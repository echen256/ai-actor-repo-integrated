from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

def make_open_ai_call(prompt):  
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_API_KEY}"
    } 
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    } 
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Success!") 
        print( response.json()['choices'][0])
        return response.json()['choices'][0]['message']['content']
    else:
        print("Request failed with status code:", response.status_code)
        print("Response Content:", response.text)
        return None

def get_cover_letter_prompt (job_description):
    # Gets the cover letter prompt by 
    with open('files/resume.txt', 'r') as resume_file:
       resume_content = resume_file.read()

    # Import cover_letter.txt
    with open('prompts/cover_letter_prompt.txt', 'r') as cover_letter_file:
        cover_letter_content = cover_letter_file.read()

    return f"""{cover_letter_content} 
            The resume is provided below" 
            {resume_content} 
            The job description is provided below 
            {job_description}"""

@app.route('/read_page', methods=['POST'])
def read_page(): 
    # This endpoint takes the raw HTML and finds the job description from it. It only works with LinkedIn pages 
    # because of the specific strings it is looking for. It could in theory do this for any page, but this optimization 
    # was done to reduce the tokens used for inference. 
    
    page_html = str(request.data)
    is_jobs_page = page_html.find("About the job")  
    if (is_jobs_page > 0 ): 
        job_description_article_start = page_html.find('<article class=')
        job_description_article_end = page_html.find("</article>") 
        prompt = get_cover_letter_prompt( page_html[job_description_article_start:job_description_article_end])
        content = make_open_ai_call(prompt)
        if (content is not None):
            return content
        else:
            return "Failed to generate letter",500
    return "Page Parsed, but was not jobs page"

@app.route('/try_click_element', methods=['POST'])
def try_click_element():  
    return "Page Parsed, but was not jobs page"


if __name__ == '__main__':
    app.run(debug=True)
