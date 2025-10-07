from flask import Flask, render_template, request
from transformers import pipeline
import datetime
import os

app = Flask(__name__)

generator = pipeline("text-generation", model="gpt2")

def ai_response(prompt):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_input = ""
    
    if request.method == "POST":
        user_input = request.form["prompt"]
        
        if "the time" in user_input.lower():
            result = f"Current time is: {datetime.datetime.now().strftime('%H:%M:%S')}"
        elif "open music" in user_input.lower():
            music_path = r"D:\Songs\Arijit Singh Best Songs BIG Playlist 2021🎶🎶🎶"
            songs = os.listdir(music_path)
            result = f"First song: {songs[0]}" if songs else "No songs found."
        elif any(site in user_input.lower() for site in ["google","youtube","github","stackoverflow","reddit"]):
            sites = {
                "google":"https://www.google.com",
                "youtube":"https://www.youtube.com",
                "stackoverflow":"https://stackoverflow.com",
                "github":"https://github.com",
                "reddit":"https://www.reddit.com"
            }
            for name,url in sites.items():
                if name in user_input.lower():
                    result = f"Open this link: <a href='{url}' target='_blank'>{name.title()}</a>"
        else:
            result = ai_response(user_input)

    return render_template("index.html", result=result, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
