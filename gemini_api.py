from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # Import CORS module

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set your Gemini API key
genai.configure(api_key="AIzaSyC443ciM76YbLOnBiQrsQ93O-fq8PblfB4")

@app.route("/ask_gemini", methods=["POST"])
def ask_gemini():
    try:
        data = request.get_json()
        user_query = data.get("query")

        if not user_query:
            return jsonify({"error": "Query is required"}), 400

        # Generate response from Gemini AI
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_query)

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
