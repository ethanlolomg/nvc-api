from flask import Flask, session, request, jsonify, make_response
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config.update(ENV='development')
app.config.update(SECRET_KEY='878as7d8f7997dfaewrwv8asdf8)(dS&A&*d78(*&ASD08A')

SESSION_KEY = "json"

def __default_message(message:str):
    new_prompt = "Rephrase in NVC: " + message

    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=new_prompt,
        max_tokens=256,
        temperature=0
    )
    print(result)
    return {"translation": result["choices"][0]["text"]}


@app.route("/get", methods=["GET"])
def get():
    get = session.get(SESSION_KEY)
    return make_response(jsonify(get), 200)


@app.route("/post", methods=["POST"])
def post():
    post = request.get_json()
    print(post)
    
    if post is not None:
        session[SESSION_KEY] = post
        return jsonify(__default_message(post["text"]), 201)
    else:
        return jsonify(__default_message(message="wrong payload"), 400)

app.run(host="127.0.0.1", port=8085, debug=True)