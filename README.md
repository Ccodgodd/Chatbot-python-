````markdown
# AI Assistant Web App

A **Flask-based AI Assistant** web application that responds to user prompts using OpenAI's GPT models (or optional free APIs) and performs additional tasks like showing current time, opening music files, and providing quick links to popular websites.

---

## Features

- **Conversational AI:** Chat with GPT-3.5-turbo (or free API alternatives).
- **Custom Commands:**
  - Get current time: type “the time”
  - Open music folder and show first song
  - Quick website links (Google, YouTube, GitHub, StackOverflow, Reddit)
- **Interactive UI:** Clean, modern web interface with hover effects and responsive design.
- **Extensible:** Easy to add new commands or integrate additional APIs.

---

## Demo

![Demo Screenshot](screenshot.png) *(optional: add your screenshot here)*

---

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **AI Integration:** OpenAI GPT API (or alternative free APIs)
- **Others:** OS module for local file handling, datetime module

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-assistant.git
   cd ai-assistant
````

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `config.py` file** with your OpenAI API key:

   ```python
   apikey = "YOUR_OPENAI_API_KEY"
   ```

5. **Run the Flask app:**

   ```bash
   python app.py
   ```

6. **Open your browser** at:

   ```
   http://127.0.0.1:5000/
   ```

---

## Folder Structure

```
ai-assistant/
├── templates/
│   └── index.html
├── static/
│   └── style.css  # optional: CSS file for styling
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Usage

* Type a question or prompt in the input box and click **Send**.
* Use specific commands like:

  * `"the time"` → Shows current time.
  * `"open music"` → Shows first song in your music folder.
  * `"open google"` → Provides a clickable link to Google.

---

## Contribution

Feel free to **fork this repository**, add new features, and submit a pull request.

---

## License

This project is licensed under the **MIT License**.

```

