from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from config import apikey

import openai
openai.api_key = apikey


app = Flask(__name__)

# connection to database
app.config["MONGO_URI"] = "mongodb+srv://LoneWolf:priyamygf12@cluster0.luv9pon.mongodb.net/FlaskGPT?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html", mychats=mychats)


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if (chat):
            data = {"result": f"{chat['answer']}"}
            
        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            mongo.db.chats.insert_one(
                {"question": question, "answer": response['choices'][0]['text']})
            data = {"result": response['choices'][0]['text']}

        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
