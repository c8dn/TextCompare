import openai
from flask import Flask, request, render_template
import os


openai.api_key = os.getenv("API_KEY")

app = Flask('app')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files['file1'].read().decode('utf-8')
    file2 = request.files['file2'].read().decode('utf-8')

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="File 1: " + file1 + ", File 2:" + file2 +"Explain what is the difference in between these 2 lines",
            temperature=0.6,
        )



    return render_template('compare.html', differences=response)



app.run(host='0.0.0.0', port=8080)