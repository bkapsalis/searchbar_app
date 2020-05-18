from flask import Flask, render_template
import toHtml



app = Flask(__name__)


@app.route("/")
def index():
	temp  = toHtml.convert()
	return render_template("index.html", htm=temp)


if __name__ == "__main__":
    app.run()
