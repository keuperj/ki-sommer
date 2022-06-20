from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

classifier = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    basket = request.json['basket']
    customerType = request.json['customerType']
    totalAmount = request.json['totalAmount']
    p = probability(basket, customerType, totalAmount)
    return jsonify({'probability': p}), 201

def probability(basket, customerType, totalAmount):
    print("Processing request: {},{},{}".format(basket, customerType, totalAmount))

    df = pd.DataFrame(data={'basket': [basket], 'totalAmount': [totalAmount], 
                  'customerType': [customerType]})

    df['customerType'] = pd.Categorical(df['customerType'], categories=["existing", "new"])


    df = pd.get_dummies(df, columns = ["customerType"], )
    df['c_0'] = df.basket.map(lambda x: x.count("0"))
    df['c_1'] = df.basket.map(lambda x: x.count("1"))
    df['c_2'] = df.basket.map(lambda x: x.count("2"))
    df['c_3'] = df.basket.map(lambda x: x.count("3"))
    df['c_4'] = df.basket.map(lambda x: x.count("4"))
    df['c_5'] = df.basket.map(lambda x: x.count("5"))

    
    df = df.drop(["basket"], axis=1)
    print(df.columns)
    p = classifier.predict(df)[0]

    return int(p)

if __name__ == "__main__":
	app.run(debug=True)
