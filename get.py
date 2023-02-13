from flask import Flask, render_template
import 

app = Flask(__name__)

@app.route("/")
def index():
    output = your_python_script.run()
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run()
