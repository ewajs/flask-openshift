from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mauro!"

@app.route("/test")
def test():
    return "<h1>This is a test!</h1>"

app.run(debug=True, host='0.0.0.0', port=8080)
