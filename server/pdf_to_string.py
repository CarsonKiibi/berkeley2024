from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def process_resume(resume_file, bio):
    # Process the resume file and bio text here
    # For demonstration purposes, we'll just return the file name and bio text
    return {'resume_file': resume_file, 'bio': bio}
@app.route('/api/submit', methods=['POST'])
def submit():
    resume = "Project with Flask and React to visually display Canadian Census Data. Project with Java Spring to allow students to plan their courses. Languages: Python, Javascript, Java, SQL. Technologies: Flask, React, VSCODE"
    jobDesc = "Job Title: Fullstack Developer (Flask/React.js) Company: ByteBurst Technologies Location: California, USA Job Description ByteBurst Technologies is seeking a talented Fullstack Developer proficient in Flask and React.js to join our dynamic team. The ideal candidate will have a strong background in both frontend and backend development, with a passion for creating innovative web solutions. Key responsibilities include developing and maintaining web applications, collaborating with cross-functional teams, and ensuring high performance and responsiveness of applications. Candidates should possess excellent problem-solving skills and a commitment to delivering high-quality work. Experience with database management systems and cloud technologies is a plus."
    load_dotenv()
    # Get the OpenAI API key from the environment variable
    key = os.getenv("OPEN_API_KEY")
    openai.api_key = (key)
    chat_completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Imagine you are interviewing a candidate with the following resume and job description" + resume + jobDesc + ". Explicitly output 3 interview questions only."}
    ],
)
    response_content = chat_completion.choices[0].message.content
    response = jsonify({'content':response_content})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    app.run(debug=True)