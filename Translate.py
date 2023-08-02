import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    text = text_entry.get()
    translation = translate(text)
    translation_label.config(text=translation)

def translate(text):
    translator = Translator()
    translated = translator.translate(text, dest='en')
    return translated.text

def main():
    global text_entry, translation_label  # Declare text_entry and translation_label as global variables

    root = tk.Tk()
    root.title("Language Translator")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), background="blue", foreground="black")

    title_label = ttk.Label(root, text="Language Translator", font=("Arial", 16, "bold"), padding=(0, 10))
    title_label.pack()

    label = ttk.Label(root, text="Enter text:")
    label.pack(pady=5)

    text_entry = ttk.Entry(root, font=("Arial", 12), width=40)
    text_entry.pack(pady=5)

    translate_button = ttk.Button(root, text="Translate", command=translate_text)
    translate_button.pack(pady=10)

    translation_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
    translation_label.pack()

    footer_label = ttk.Label(root, text="Made By Fahad", font=("Arial", 10, "italic"), padding=(0, 10))
    footer_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
