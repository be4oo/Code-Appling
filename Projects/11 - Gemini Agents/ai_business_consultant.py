# File: ai_business_consultant.py

import google.generativeai as genai
import json
import re

def generate_chat_response(system_content, user_content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[
        {'role': 'user', 'parts': [system_content]},
        {'role': 'model', 'parts': ["Understood. I'll proceed as instructed."]}
    ])
    response = chat.send_message(user_content, generation_config=genai.types.GenerationConfig(
        max_output_tokens=2000
    ))
    return response

def extract_json(response_content):
    pattern = r'```json\n(.*?)```'
    matches = re.findall(pattern, response_content, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    return None

def business_consultant(idea_description):
    system_content = """
    You are an experienced business consultant AI. Your task is to analyze business ideas and provide 
    comprehensive feedback. For each idea, you should return a JSON object with the following structure:

    {
        "analysis": "Brief analysis of the idea",
        "success_probability": "A percentage between 0 and 100",
        "team_skills": ["List of required skills for the team"],
        "mvp_tips": ["List of tips for creating a Minimum Viable Product"],
        "business_model": "Brief description of a suitable business model",
        "swot_analysis": {
            "strengths": ["List of strengths"],
            "weaknesses": ["List of weaknesses"],
            "opportunities": ["List of opportunities"],
            "threats": ["List of threats"]
        }
    }

    Provide thoughtful and actionable insights for each field. The success probability should be based on 
    market potential, innovation, and feasibility. Ensure all responses are wrapped in a JSON code block.
    """

    user_content = f"Analyze the following business idea: {idea_description}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        analysis_result = extract_json(response_content)

        if analysis_result is None:
            return {"error": "Failed to generate or parse the analysis."}

        return analysis_result

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    idea = "A mobile app that connects local farmers directly with consumers for fresh produce delivery"
    result = business_consultant(idea)
    print(json.dumps(result, indent=2))