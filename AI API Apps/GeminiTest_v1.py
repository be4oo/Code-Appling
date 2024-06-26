from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GEMINI_API_KEY')  # Assuming you have a 'TOKEN' in your .env file
bard = Bard(token=token)

result = bard.get_answer("What is the current stock price of WDA?")  # Assuming 'get_stock_price' is a method in Bard class 
print(result)