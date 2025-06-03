from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Example poem responses
poems = {
    "madness": [
        "Sanity is the cruelest delusion of all.",
        "A pen is a dagger that dreams in ink."
    ],
    "grief": [
        "Where she once stood, silence now blooms.",
        "Tears are letters the soul sends nowhere."
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_poem():
    theme = request.json.get('theme', '').lower()
    response = random.choice(poems.get(theme, ["The muse weeps in silence..."]))
    return jsonify({'poem': response})

if __name__ == '__main__':
    app.run(debug=True)
