# 📝 Flask Blog Generator

This is a simple web-based **blog paragraph generator** built with **Flask** and the **OpenAI GPT-3.5 API**.  
Just enter a topic, and the AI will generate a paragraph about it, displayed instantly on a clean web interface.

## 🚀 Features

- ✅ Enter a topic and get an AI-generated paragraph
- ✅ Uses OpenAI GPT-3.5 Turbo model
- ✅ Clean and responsive web UI with HTML/CSS
- ✅ Built with Flask for easy Python backend
- ✅ API key is safely managed with dotenv

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/flask-blog-generator.git
cd flask-blog-generator

2️⃣ Install dependencies

pip install -r requirements.txt

Or manually:

pip install flask openai python-dotenv

3️⃣ Add your OpenAI API key

Create a file named api_key.env (or .env) in the root directory with the following content:

API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

⚠️ Important: Do not share this file or commit it to GitHub.

4️⃣ Start the Flask server

python app.py

Visit http://127.0.0.1:5000 in your browser.

🖼 Example Output

Input:

Topic: Travel

Output:

Travel opens the door to new experiences, cultures, and connections. It broadens our perspectives and reminds us how diverse and beautiful the world truly is...

📁 Project Structure

flask-blog-generator/
├── app.py               # Main Flask application
├── api_key.env          # 🔐 Your OpenAI API key (should be ignored by Git)
├── .gitignore           # Files/folders not to be tracked by Git
├── requirements.txt     # Python dependencies
└── templates/
    └── index.html       # Front-end web interface


📌 .gitignore (Recommended)

Prevent sensitive files like your API key from being pushed to GitHub:

__pycache__/
api_key.env
.env
*.pyc


💡 To Do / Ideas for Improvement
	•	Add copy-to-clipboard button ✂️
	•	Export generated text to .txt file
	•	Support multi-paragraph blog posts
	•	Add themes (e.g. Dark Mode 🌙)
	•	Add language selection dropdown


🛠 Built With
	•	Flask
	•	OpenAI API
	•	Python-dotenv
