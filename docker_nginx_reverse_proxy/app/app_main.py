from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Main Page </p>"

@app.route("/api")
def api():

    return f"<p>API for app 1</p> <div>{request.path}</div><div>{request.url}</div>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)