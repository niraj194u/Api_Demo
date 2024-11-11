# calculator_api.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify({"result": result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({"result": result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    result = data['a'] / data['b']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
