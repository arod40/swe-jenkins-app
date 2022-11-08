from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/person", methods=["GET"])
def person_endpoint():
    return jsonify([{"name": "p1", "email": "p1@domain.com"},{"name": "p2", "email": "p2@domain.com"},{"name": "p3", "email": "p3@domain.com"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
