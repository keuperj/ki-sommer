from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    basket = request.json['basket']
    customerType = request.json['customerType']
    totalAmount = request.json['totalAmount']
    p = probability(basket, customerType, totalAmount)
    return jsonify({'probability': p}), 201

def probability(basket, customerType, totalAmount):
    print("Processing request: {},{},{}".format(basket, customerType, totalAmount))
    return 0.0

if __name__ == "__main__":
	app.run(debug=True)
