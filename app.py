from flask import Flask, render_template, jsonify, request
from rapidfuzz import fuzz
import json

app = Flask(__name__)

# Load Q&A Data
with open("qa_data.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Categories API
@app.route("/api/categories")
def categories():

    categories = {}

    for item in qa_data:

        cat = item.get("category", "General")

        if cat not in categories:

            categories[cat] = {
                "id": cat,
                "name": cat,
                "icon": item.get("icon", "📁")
            }

    return jsonify(list(categories.values()))

# Questions By Category
@app.route("/api/questions/<category>")
def questions(category):

    results = []

    for index, item in enumerate(qa_data):

        if item.get("category") == category:

            results.append({
                "id": index,
                "question": item["question"]
            })

    return jsonify(results)

# Answer API
@app.route("/api/answer/<int:q_id>")
def answer(q_id):

    item = qa_data[q_id]

    return jsonify({
        "question": item["question"],
        "answer": item["answer"],
        "category": item.get("category", "General")
    })

# Smart Search
@app.route("/api/search", methods=["POST"])
def search():

    data = request.get_json()

    query = data.get("query", "").lower()

    best_score = 0
    best_match = None

    for item in qa_data:

        score = fuzz.partial_ratio(
            query,
            item["question"].lower()
        )

        if score > best_score:

            best_score = score
            best_match = item

    if best_score >= 60:

        return jsonify({
            "found": True,
            "result": {
                "question": best_match["question"],
                "answer": best_match["answer"],
                "category": best_match.get("category", "General")
            }
        })

    return jsonify({
        "found": False
    })

# Run App
if __name__ == "__main__":
    app.run(debug=True)