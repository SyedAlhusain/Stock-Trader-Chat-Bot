from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key="insert-your-api-key-here")

# Function to get AI response
def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for handling user input and displaying response
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() == "quit":
        return "Goodbye!"
    response = chat_gpt("Pretend you're a stock trader bro and answer me this question: " + user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
