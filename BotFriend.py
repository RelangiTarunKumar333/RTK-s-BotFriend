import os
import tkinter as tk
from tkinter import scrolledtext
from groq import Groq

# Set the API key for Groq
os.environ['GROQ_API_KEY'] = "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"

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat with Groq")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')

        # Unique Heading
        self.heading_frame = tk.Frame(root, bg='#34495e', pady=10)
        self.heading_frame.pack(fill=tk.X)
        self.heading_label = tk.Label(self.heading_frame, text="Chat with Groq", font=("Helvetica", 24, "bold"), fg='#ecf0f1', bg='#34495e')
        self.heading_label.pack()

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg='#ecf0f1', fg='#2c3e50', font=("Helvetica", 12), padx=10, pady=10)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.user_input_frame = tk.Frame(root, bg='#2c3e50')
        self.user_input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.user_input = tk.Entry(self.user_input_frame, font=("Helvetica", 14), bg='#ecf0f1', fg='#2c3e50', relief=tk.GROOVE, bd=2)
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.user_input_frame, text="Send", command=self.send_message, font=("Helvetica", 14, "bold"), bg='#3498db', fg='#ecf0f1', activebackground='#2980b9', relief=tk.RAISED, bd=2)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.add_message("Bot", "Hello! Let's chat.\nYou can type 'bye', 'exit', or 'end' to stop the conversation.")

        # Initialize Groq client
        self.client = Groq()

    def add_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

    def send_message(self, event=None):
        user_message = self.user_input.get()
        if user_message.lower() in ['bye', 'exit', 'end']:
            self.add_message("Bot", "Goodbye! Have a great day!")
            self.root.after(2000, self.root.destroy)  # Close the window after 2 seconds
            return

        self.add_message("You", user_message)
        self.user_input.delete(0, tk.END)

        response = self.get_bot_response(user_message)
        self.add_message("Bot", response)

    def get_bot_response(self, message):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: Unable to get response from Groq API. {e}"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
