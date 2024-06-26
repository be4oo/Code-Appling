import tkinter as tk
from tkinter import scrolledtext

class TextOrganizer:
    def __init__(self):
        self.texts = {}
        self.model_counter = 1

    def add_text(self, text):
        model_name = f"Model {self.model_counter} answer"
        self.texts[model_name] = text
        self.model_counter += 1

    def get_organized_text(self):
        organized_text = ""
        for model_name, text in self.texts.items():
            organized_text += f"{model_name}\n\"{text}\"\n"
        return organized_text

    def clear_texts(self):
        self.texts = {}
        self.model_counter = 1


def add_text(event=None):
    text = text_entry.get()
    organizer.add_text(text)
    text_entry.delete(0, 'end')
    update_text()

def update_text():
    organized_text.delete(1.0, 'end')
    organized_text.insert('insert', organizer.get_organized_text())

def clear_texts():
    organizer.clear_texts()
    update_text()

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(organizer.get_organized_text())


organizer = TextOrganizer()

root = tk.Tk()

text_entry = tk.Entry(root)
text_entry.pack()
text_entry.bind('<Return>', add_text)

add_button = tk.Button(root, text="Add Text", command=add_text)
add_button.pack()

clear_button = tk.Button(root, text="Clear Texts", command=clear_texts)
clear_button.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

organized_text = scrolledtext.ScrolledText(root)
organized_text.pack()

root.mainloop()