import tkinter as tk
import random

def get_random_joke(jokes_list):
    return random.choice(jokes_list)

def update_joke_text(text_widget, jokes_list):
    joke = get_random_joke(jokes_list)
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, joke)

def next_joke(text_widget, jokes_list):
    current_joke = text_widget.get('1.0', tk.END).strip()
    index = jokes_list.index(current_joke)
    next_index = (index + 1) % len(jokes_list)
    next_joke = jokes_list[next_index]
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, next_joke)

def main():
    root = tk.Tk()
    root.title("Alexa, Tell Me a Joke")

    # Create a frame to hold the text widget and buttons
    frame = tk.Frame(root)
    frame.pack()

    # Create a text widget to display the joke
    text_widget = tk.Text(frame, height=5, width=40)
    text_widget.pack(pady=10)

    # Create a button to get a new random joke
    joke_button = tk.Button(frame, text="Get a Joke", command=lambda: update_joke_text(text_widget, jokes_list))
    joke_button.pack(side=tk.LEFT)

    # Create a button to display the next joke in the list
    next_button = tk.Button(frame, text="Next Joke", command=lambda: next_joke(text_widget, jokes_list))
    next_button.pack(side=tk.RIGHT)

    # Read jokes from the file
    with open("randomJokes.txt", "r") as f:
        jokes_list = f.readlines()

    # Display the initial joke
    update_joke_text(text_widget, jokes_list)

    root.mainloop()

if __name__ == "__main__":
    main()