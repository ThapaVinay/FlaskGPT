from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)


# connection to database
mongo = PyMongo(app)
app.config["MONGO_URI"] = "mongodb+srv://LoneWolf:priyamygf12@cluster0.luv9pon.mongodb.net/FlaskGPT?retryWrites=true&w=majority"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        data = {"result":question}

    return jsonify(data)

app.run(debug = True)