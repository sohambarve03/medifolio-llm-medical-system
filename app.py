
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


# Simulate a database (in-memory for simplicity)
patients = {
    "123": {"name": "John Doe", "history": ["Diabetes Diagnosis", "Allergy to Penicillin"]},
}

# Storage for prescriptions
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# API Endpoints
@app.route("/api/chat", methods=["POST"])
def chat():
    """Hardcoded chat response"""
    user_message = request.json.get("message", "")
    response = {
        "response": f"I see you said: '{user_message}'. This is a placeholder response."
    }
    return jsonify(response)

@app.route("/api/doctors", methods=["GET"])
def get_doctors():
    """Return hardcoded list of doctors"""
    doctors = [
        {"name": "Dr. Smith", "specialty": "Cardiologist", "rating": 4.8},
        {"name": "Dr. Patel", "specialty": "Dermatologist", "rating": 4.5},
    ]
    return jsonify(doctors)

if __name__ == "__main__":
    app.run(debug=True)
