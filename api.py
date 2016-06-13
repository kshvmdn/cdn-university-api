from flask import Flask, request, jsonify, render_template, abort
from scraper import scrape

app = Flask(__name__)
app.config['JSON_SORT_KEYS']


@app.route('/')
@app.route('/api')
def root():
    return render_template('index.html')


@app.route('/api/<code>')
def api(code):
    try:
        data = scrape(code)
    except:
        data = None

    if not data:
        abort(404, {'message': 'Couldn\'t retrieve data for program %s.' % code})

    return jsonify(meta=dict(status=200, message='OK'), data=data)


@app.errorhandler(400)
@app.errorhandler(404)
def bad_request(error):
    status, message = error.code, error.description['message']

    response = jsonify(meta=dict(status=status, message=message), data=None)
    return response, error.code

if __name__ == "__main__":
    import os
    port = os.environ.get('PORT', 8000)
    app.run(host='127.0.0.1', port=int(port), debug=True)
