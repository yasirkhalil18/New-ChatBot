from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "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"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def ask_deepseek(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = ask_deepseek(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
