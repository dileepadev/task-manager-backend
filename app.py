from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded news data
news_data = [
    {"id": 1, "title": "Breaking News 1", "content": "Lorem ipsum dolor sit amet..."},
    {"id": 2, "title": "Breaking News 2", "content": "Consectetur adipiscing elit..."},
    {
        "id": 3,
        "title": "Breaking News 3",
        "content": "Sed do eiusmod tempor incididunt...",
    },
]


# Endpoint to get all news articles
@app.route("/api/news", methods=["GET"])
def get_news():
    return jsonify(news_data)


# Endpoint to add a new news article
@app.route("/api/news", methods=["POST"])
def add_news():
    data = request.json
    new_article = {
        "id": len(news_data) + 1,
        "title": data.get("title"),
        "content": data.get("content"),
    }
    news_data.append(new_article)
    return jsonify(new_article), 201


if __name__ == "__main__":
    app.run(debug=True)
