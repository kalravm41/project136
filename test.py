from flask import Flask, jsonify
from d import data
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'Data': data,
        'Message': 'Success!!'
    }),200

if __name__ == '__main__':
    app.run()