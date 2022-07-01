from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='View')
Bootstrap(app)


@app.route("/")
def home():
    html = render_template("index.html")
    return html

@app.route("/projetos")
def projetos():
    html = ""
    return html

if __name__ == "__main__":
    app.run(debug=True)
