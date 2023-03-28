from flask import Flask, session, request, jsonify, render_template
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config.update(ENV='development')
app.config.update(SECRET_KEY='878as7d8f7997dfaewrwv8asdf8)(dS&A&*d78(*&ASD08A')

SESSION_KEY = "json"

def __default_message(message:str):
    new_prompt = "Rephrase in NVC language " + message

    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=new_prompt,
        max_tokens=3000,
        temperature=1.2
    )
    print(result)
    return {"translation": result["choices"][0]["text"]}


@app.route('/')
def home():
   return render_template("index.html")

@app.route("/translate", methods=["GET"])
def get():
    # get = session.get(SESSION_KEY)
    text = request.args.get("text")
    response = jsonify(__default_message(text), 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response # For some reason the response comes back with leading \n's; trimming in js for now


@app.route("/post", methods=["POST"])
def post():
    post = request.get_json()
    print(post)
    
    if post is not None:
        session[SESSION_KEY] = post
        return jsonify(__default_message(post["text"]), 201)
    else:
        return jsonify(__default_message(message="wrong payload"), 400)

app.run(host="127.0.0.1", port=5001, debug=True) # uncomment to run locally #runningLocally #ref