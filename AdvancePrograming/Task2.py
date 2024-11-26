import tkinter as tk
import random

def get_random_joke(jokes):
    return random.choice(jokes).strip()

def tell_joke(text_area, jokes):
    joke = get_random_joke(jokes)
    if '?' in joke:
        setup, punchline = joke.split('?', 1)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"{setup}?\n\nPress Enter to see the punchline...")
        text_area.bind("<Return>", lambda event: show_punchline(text_area, punchline))
    else:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Invalid joke format.")

def show_punchline(text_area, punchline):
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, punchline)

root = tk.Tk()
root.title("Alexa, Tell Me a Joke!")

welcome_label = tk.Label(root, text="Welcome! Press the button below to hear a random joke.")
welcome_label.pack(pady=10)

text_area = tk.Text(root, height=5, width=40)
text_area.pack(pady=10)

joke_button = tk.Button(root, text="Tell Me a Joke!", command=lambda: tell_joke(text_area, jokes))
joke_button.pack()

try:
    with open("randomjokes.txt", "r") as joke_file:
        jokes = joke_file.readlines()
except FileNotFoundError:
    jokes = []
    text_area.insert(tk.END, "Error: Jokes file not found.")

root.mainloop()
