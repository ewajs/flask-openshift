from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mauro!"

app.run(debug=True, host='0.0.0.0', port=8080)
