from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "TaskForge API"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "TaskForge API"
    })

if __name__ == "__main__":
    app.run(debug=True)