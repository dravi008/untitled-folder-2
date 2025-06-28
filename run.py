import os
from dotenv import load_dotenv
load_dotenv()

import openai
from flask import Flask, render_template, request, jsonify
# --- Flask setup ---
app = Flask(__name__, template_folder="FlightDebriefAI/templates")

# --- Route: Test AI debrief ---
@app.route('/debrief', methods=['POST'])
def generate_debrief():
    data = request.json
    maneuvers = data.get('maneuvers', [])
    notes = data.get('notes', '')

    prompt = f"Create a flight instructor debrief. Maneuvers: {maneuvers}. Notes: {notes}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're an FAA-certified flight instructor giving a structured student debrief."},
                  {"role": "user", "content": prompt}]
    )

    return jsonify({
        "debrief": response.choices[0].message['content']
    })

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)