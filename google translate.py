import tkinter as tk
from tkinter import ttk
from googletrans import Translator


def translate_text():
    text_to_translate = source_text.get("1.0", "end-1c")  # Get text from the source_text Text widget
    source_language = source_language_combobox.get()
    dest_language = dest_language_combobox.get()

    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=source_language, dest=dest_language)

    result_text.delete("1.0", "end")  # Clear the result_text Text widget
    result_text.insert("1.0", translated_text.text)  # Display the translated text


app = tk.Tk()
app.title("Multilingual Text Translator")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10)

source_label = ttk.Label(frame, text="Enter Text:")
source_label.grid(row=0, column=0, sticky="w")

source_text = tk.Text(frame, width=40, height=5)
source_text.grid(row=1, column=0, padx=5, pady=5)

source_language_label = ttk.Label(frame, text="Source Language:")
source_language_label.grid(row=2, column=0, sticky="w")

source_language_combobox = ttk.Combobox(frame, values=["en", "hi", "es", "fr", "de", "zh-CN"], width=10)
source_language_combobox.set("en")
source_language_combobox.grid(row=3, column=0, padx=5, pady=5)

dest_language_label = ttk.Label(frame, text="Destination Language:")
dest_language_label.grid(row=4, column=0, sticky="w")

dest_language_combobox = ttk.Combobox(frame, values=["en", "hi", "es", "fr", "de", "zh-CN"], width=10)
dest_language_combobox.set("hi")
dest_language_combobox.grid(row=5, column=0, padx=5, pady=5)

translate_button = ttk.Button(frame, text="Translate", command=translate_text)
translate_button.grid(row=6, column=0, padx=5, pady=5)

result_label = ttk.Label(frame, text="Translated Text:")
result_label.grid(row=3, column=0, sticky="w")

result_text = tk.Text(frame, width=40, height=5)
result_text.grid(row=4, column=0, padx=5, pady=5)

app.mainloop()
