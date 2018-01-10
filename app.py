from flask import Flask, current_app, jsonify
import markov_gen

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def hello_world():
    return current_app.send_static_file('index.html')


@app.route('/comments')
def comments():
    return jsonify(filter(None,list(markov_gen.generate(5, 'tulevik'))))

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)