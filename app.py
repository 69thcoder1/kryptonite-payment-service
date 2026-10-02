from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Kryptonite Payment Service",
        "status": "running",
        "environment": "production"
    })

@app.route("/payments")
def payments():
    return jsonify({
        "service": "payment",
        "status": "ready"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
