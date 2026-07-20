from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return "NutriScan AI Server Running"


@app.route("/scan", methods=["POST"])
def scan_food():

    if "image" not in request.files:
        return jsonify({
            "error": "Image nahi mili"
        })

    image = request.files["image"]

    path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(path)


    # Abhi demo result
    result = {
        "food": "Unknown",
        "score": "Checking...",
        "message": "AI analysis starting"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
