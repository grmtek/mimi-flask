import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
#    name = os.environ.get("NAME", "Human")
#    return "Hello {}, welcome to Mimi's Life on Mars!".format(name)
     return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))