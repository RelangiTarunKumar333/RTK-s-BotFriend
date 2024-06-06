# ChatBot Application using Tkinter and Groq API

This repository contains a simple graphical chat application built with Python's Tkinter library. The application connects to a chatbot service using the Groq API, allowing users to interact with an AI-powered bot.

## Features

- **Graphical User Interface**: Designed with Tkinter, featuring a chat display, user input field, and send button.
- **Groq API Integration**: Communicates with the Groq chatbot service to generate responses.
- **Customizable Design**: Includes different styles and layouts for the chat window.
- **User-Friendly**: Easy to use, with support for common exit commands (bye, exit, end).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Groq API key**:
    - Obtain your API key from Groq.
    - Set the environment variable `GROQ_API_KEY` with your key:
        ```bash
        export GROQ_API_KEY="your_groq_api_key"  # On Windows, use `set` instead of `export`
        ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Interact with the chatbot**:
    - Type your message in the input field and press Enter or click the "Send" button.
    - The bot will respond, and the conversation will be displayed in the chat window.
    - To end the conversation, type "bye", "exit", or "end".

## File Structure

- `app.py`: The main script containing the Tkinter application and Groq API integration.
- `requirements.txt`: List of Python packages required for the application.
- `.gitignore`: Git ignore file for excluding unnecessary files from version control.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library.
- [Groq](https://groq.com/) - AI chatbot service used for generating responses.

---

Feel free to customize the design and functionality as per your needs. Contributions are welcome!

