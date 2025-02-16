from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Test Analysis API is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    answers = data.get("answers", {})
    correct_answers = {
        "q1": "A", "q2": "C", "q3": "B", "q4": "D", "q5": "A"
    }

    wrong_answers = []
    correct_count = 0

    for key in correct_answers:
        if answers.get(key) != correct_answers[key]:
            wrong_answers.append(f"{key}: Дұрыс жауап - {correct_answers[key]}")
        else:
            correct_count += 1

    motivation = "Жарайсың! Келесі жолы одан да жақсы нәтиже көрсетесің! 🚀" if correct_count < len(correct_answers) else "Керемет! Барлық сұрақтарға дұрыс жауап бердің! 🎉"

    return jsonify({"wrong_answers": wrong_answers, "correct_count": correct_count, "motivation": motivation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
