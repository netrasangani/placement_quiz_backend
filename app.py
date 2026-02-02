from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

questions = [
    {
        "id": 1,
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree"],
        "answer": "Queue"
    },
    {
        "id": 2,
        "question": "What does HTTP stand for?",
        "options": [
            "Hyper Text Transfer Protocol",
            "High Transfer Text Protocol",
            "Hyperlink Transfer Tool"
        ],
        "answer": "Hyper Text Transfer Protocol"
    },
    {
        "id": 3,
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def"],
        "answer": "def"
    }
]

@app.route("/")
def home():
    return {"message": "Placement Prep Quiz Backend Running"}

@app.route("/quiz", methods=["GET"])
def get_quiz():
    return jsonify([
        {
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        } for q in questions
    ])

@app.route("/submit", methods=["POST"])
def submit_quiz():
    user_answers = request.json
    score = 0

    for q in questions:
        if user_answers.get(str(q["id"])) == q["answer"]:
            score += 1

    return {
        "score": score,
        "total": len(questions)
    }

if __name__ == "__main__":
    app.run()
