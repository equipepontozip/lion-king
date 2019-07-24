from flask import Flask
from flask import jsonify
from flask import request

from classifier import keystroke_classifier


app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'ok'})


@app.route('/keystroke', methods=['POST'])
def keystroke():
    req_dict = request.get_json()

    classification = keystroke_classifier(req_dict)

    return jsonify({'classification': classification})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
