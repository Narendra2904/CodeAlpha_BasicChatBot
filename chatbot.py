import tkinter as tk
from tkinter import scrolledtext

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "good morning", "good afternoon"]:
        return "Hello! How can I help you?"
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm doing well, thanks for asking!"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot."
    elif user_input in ["help", "can you help me", "i need help"]:
        return "Sure! What do you need help with?"
    elif user_input in ["thanks", "thank you", "thx"]:
        return "You're welcome!"
    elif user_input in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you try something else?"

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

    entry.delete(0, tk.END)

    if user_input.lower().strip() in ["bye", "goodbye", "exit", "see you"]:
        root.after(1000, root.quit)

root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")

chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=5, fill=tk.X)

entry = tk.Entry(entry_frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.focus()

send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.RIGHT)

root.bind("<Return>", lambda event: send_message())

chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "🤖 Bot: Hello! Type something to start chatting.\n\n")
chat_window.config(state=tk.DISABLED)

root.mainloop()
