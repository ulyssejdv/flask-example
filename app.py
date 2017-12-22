import json

from flask import Flask, jsonify

app = Flask(__name__)


USER_LIST = [
    "ulysse",
    "romain",
    "usman",
    "boubacar"
]


@app.route('/users')
def get_users():
    return jsonify(USER_LIST)


if __name__ == '__main__':
    app.run()
