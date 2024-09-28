import tkinter as tk
from tkinter import filedialog
from fuzzywuzzy import fuzz

def display_text_from_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filename:
        try:
            with open(filename, 'r') as file:
                text = file.read()
                text_widget.delete(1.0, tk.END)  # Clear previous text
                text_widget.insert(tk.END, text)
        except FileNotFoundError:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, "File not found!")

def display_user_text():
    user_text = user_input.get()
    match_found = False
    text_widget.delete(1.0, tk.END)  # Clear previous text
    for item in text_list:
        similarity_score = fuzz.partial_ratio(user_text, item)
        if similarity_score >= 70:  # Adjust threshold as needed
            text_widget.insert(tk.END, f"Match found: {item}\n")
            match_found = True
    if not match_found:
        text_widget.insert(tk.END, "No match found.")

# Create the Tkinter window
root = tk.Tk()
root.title("Display Text")

# Create a Text widget to display the text
text_widget = tk.Text(root, wrap="word")
text_widget.pack(fill="both", expand=True)

# Create a Browse button
browse_button = tk.Button(root, text="Browse", command=display_text_from_file)
browse_button.pack()

# Create an Entry widget for user input
user_input = tk.Entry(root)
user_input.pack()

# Create a button to display user input
display_button = tk.Button(root, text="Display User Input", command=display_user_text)
display_button.pack()

# List of texts from the file
text_list = []

# Start the Tkinter event loop
root.mainloop()
