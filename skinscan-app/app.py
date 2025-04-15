from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
import base64  # Import base64 for encoding binary data

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Groq client with API key from .env
client = Groq(api_key=os.getenv("GROQ_API"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login logic here
        email = request.form["email"]
        password = request.form["password"]
        # For now, just redirect to the upload page
        return render_template("upload.html")
    return render_template("login.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    try:
        # Read the binary image data and encode it in Base64
        image_base64 = base64.b64encode(image.read()).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{image_base64}"
    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

    try:
        # Use the Groq API to analyze the image
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "analyze image for skinproblems and suggest skincare\n"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        # Access the content correctly
        response = completion.choices[0].message.content
    except Exception as e:
        return jsonify({"error": f"Groq API call failed: {str(e)}"}), 500

    return render_template("results.html", analysis=response)

@app.route("/results", methods=["POST"])
def results():
    # Assume `analysis` is passed from the `/analyze` route
    analysis = request.form.get("analysis", "No analysis available.")
    return render_template("results.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)