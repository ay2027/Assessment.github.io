import tkinter as tk
import random

def get_random_joke(jokes):
    return random.choice(jokes)

def tell_joke(text_area, jokes):
    joke = get_random_joke(jokes)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, joke)

# Main program starts here
root = tk.Tk()
root.title("Alexa, Tell Me a Joke!")

# Welcome message
welcome_label = tk.Label(root, text="Welcome! Press the button below to hear a random joke.")
welcome_label.pack(pady=10)

# Text area to display the joke
text_area = tk.Text(root, height=5, width=40)
text_area.pack(pady=10)

# Button to tell a joke
joke_button = tk.Button(root, text="Tell Me a Joke!", command=lambda: tell_joke(text_area, jokes))
joke_button.pack()

# Read jokes from a file (replace "randomJokes.txt" with your file path)
with open("randomJokes.txt", "r") as joke_file:
    jokes = joke_file.readlines()

root.mainloop()