from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values

app = Flask(__name__)
config = dotenv_values("/Users/jeff/Desktop/api_key.env")

#API Keys
openai.api_key = config["API_KEY"]

def generate_blog(topic):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog-writing assistant."},
            {"role": "user", "content": f"Write a blog paragraph about: {topic}"}
        ],
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    blog_text = ""
    topic = ""

    if request.method == "POST":
        topic = request.form["topic"]
        blog_text = generate_blog(topic)

    return render_template("index.html", blog_text=blog_text, topic=topic)

if __name__ == "__main__":
    app.run(debug=True)
