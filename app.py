from flask import Flask, render_template, request
import openai

# Set your OpenAI API key here
OPENAI_API_KEY = "OpenAI API key"

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            response = generate_response(user_input)
            return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html", user_input="", response="")

def generate_response(user_input):
    # GPT-3.5 inference
    prompt = "User: " + user_input + "\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
