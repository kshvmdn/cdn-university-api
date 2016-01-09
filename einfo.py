import os

from flask import Flask, request, jsonify, render_template
from scraper import scrape

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/api')
def api():
    prog_code = request.args.get('c', 1, type=int)
    program = scrape(prog_code)
    if program:
        response = jsonify(meta=dict(status=200, message="OK"), data=program)
    else:
        response = jsonify(meta=dict(status=400, message="Bad Request - no data found for program `{0}`".format(prog_code)))
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
