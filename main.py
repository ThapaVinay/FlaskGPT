from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET", "POST"])
def qa():
    # if request.method == "POST":
    data = {"result" : "how are you"}
    
    return jsonify(data)


app.run(debug = True)