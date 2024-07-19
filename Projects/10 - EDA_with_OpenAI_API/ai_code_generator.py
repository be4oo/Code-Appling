# File: ai_code_generator.py

import pandas as pd
import numpy as np
import os
import openai
from dotenv import load_dotenv
import json
import re
import google.generativeai as genai
import traceback

def generate_chat_response(system_content, user_content):
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[
        {'role': 'user', 'parts': [system_content]},
        {'role': 'model', 'parts': ["Understood. I'll proceed as instructed."]}
    ])
    response = chat.send_message(user_content, generation_config=genai.types.GenerationConfig(
        max_output_tokens=1200
    ))
    return response

def extract_code(response_content):
    pattern = r'```(.*?)```'
    matches = re.findall(pattern, response_content, re.DOTALL)
    return matches[0].replace("python", "")

def generate_code_and_execute(user_content, max_retries=3, execute=True):
    system_content = """
    You are a python code generator. You know pandas. You answer to every question with Python code.
    You return python code wrapped in ``` delimiter. Import any needed python module. And you don't provide any elaborations.
    """
    for attempt in range(max_retries):
        try:
            response = generate_chat_response(system_content, user_content)
            response_content = response.text
            code = extract_code(response_content)
            if execute:
                exec(code, globals())
            return code
        except Exception as e:
            error_message = f"Error in attempt {attempt + 1}: {str(e)}\n{traceback.format_exc()}"
            print(error_message)
            if attempt < max_retries - 1:
                user_content = f"""
                The previous code generated had an error. Please provide a corrected version.
                Error details:
                {error_message}
                Original request:
                {user_content}
                """
            else:
                print(f"Failed to generate valid code after {max_retries} attempts.")
                return None
    return None

def update_code(code, user_content, max_retries=3, execute=True, verbose=True):
    system_content = f"""
    You are a python code generator. You know pandas. You are given the following python method: {code}. Update the code based on the user content. Do not change the method name.
    You return the updated python code wrapped in ``` delimiter. And you don't provide any elaborations.
    """
    for attempt in range(max_retries):
        try:
            response = generate_chat_response(system_content, user_content)
            new_code = extract_code(response.text)
            if not new_code:
                raise ValueError("No code was generated")
            if execute:
                exec(new_code, globals())
            if verbose:
                print(f"Successfully updated and executed code on attempt {attempt + 1}")
            return new_code
        except Exception as e:
            error_message = f"Error in attempt {attempt + 1}: {str(e)}\n{traceback.format_exc()}"
            if verbose:
                print(error_message)
            if attempt < max_retries - 1:
                user_content = f"""
                The previous code update had an error. Please provide a corrected version.
                Original code:
                {code}
                Error details:
                {error_message}
                Update request:
                {user_content}
                """
            elif verbose:
                print(f"Failed to generate valid code after {max_retries} attempts.")
    return None