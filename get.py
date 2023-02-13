from flask import Flask, render_template
import slackapi

app = Flask(__name__)

@app.route("/")
def index():
    output = slackapi.run()
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run()
