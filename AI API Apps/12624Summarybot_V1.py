# Import the Python SDK
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up your API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Initial prompt
initial_prompt = """
As a skilled article and essay writer, your task is to summarize the provided text and organize it into Level 2 markdown headings. 
Following each summarizing sentence, include bullet points that accurately summarize the text without adding any additional information. 
Your output should be in markdown format and adhere to the specified rules.
"""

# Get input text from user
text = input("Enter the text you want to summarize: ")

# Prepend initial prompt to input text
text = initial_prompt + text

# Generate summary
response = model.generate_content(text)

# Print the summary
print(response.text)