import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyperclip

# Load environment variables from .env file
load_dotenv()

# Set up your API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Initial prompt
initial_prompt = """
your typing style should include the following characteristicsStructured: You tend to organize your thoughts in a clear and logical manner, often using bullet points to break down complex information into digestible parts.Analytical: You analyze situations by considering various outcomes and consequences, presenting both the positive and negative aspects of a scenario.Direct: Your communication is straightforward, getting to the point without unnecessary embellishment.Inquisitive: You use questions effectively to explore topics and guide the conversation.Balanced: You maintain a balance between a formal tone and conversational language, making your writing professional yet accessible.Detailed: You provide specific examples and details to support your points, ensuring clarity and depth in your explanations.Continue to apply these elements to your responses to align with my preferred communication style.so please keep all your coming answers with that style

organize and summarize that text, keep it on points andsub-pointss
"""

def summarize_text():
    text = text_input.get('1.0', 'end')
    text = initial_prompt + text
    response = model.generate_content(text)
    text_output.delete('1.0', 'end')
    text_output.insert('1.0', response.text)

def clear_fields():
    text_input.delete('1.0', 'end')
    text_output.delete('1.0', 'end')

def copy_to_clipboard():
    text = text_output.get('1.0', 'end')
    pyperclip.copy(text)
    messagebox.showinfo("Copied", "Text copied to clipboard")

def save_to_file():
    text = text_output.get('1.0', 'end')
    with open('output.txt', 'w') as f:
        f.write(text)
    messagebox.showinfo("Saved", "Text saved to output.txt")

root = tk.Tk()
root.title("Text Summarizer")

tk.Label(root, text="Input Text:").pack()
text_input = scrolledtext.ScrolledText(root, width=50, height=10)
text_input.pack()

tk.Button(root, text="Summarize", command=lambda: threading.Thread(target=summarize_text).start()).pack()
tk.Button(root, text="Clear", command=clear_fields).pack()

tk.Label(root, text="Output Text:").pack()
text_output = scrolledtext.ScrolledText(root, width=50, height=10)
text_output.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()
tk.Button(root, text="Save to File", command=save_to_file).pack()

root.mainloop()