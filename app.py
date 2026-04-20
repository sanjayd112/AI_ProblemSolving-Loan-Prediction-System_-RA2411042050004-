from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

model = pickle.load(open("loan_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    income = float(request.form['income'])
    credit = float(request.form['credit'])
    employment = request.form['employment']
    loan = float(request.form['loan'])

    emp = encoder.transform([employment])[0]

    data = np.array([[income, credit, emp, loan]])
    data = scaler.transform(data)

    result = model.predict(data)

    output = "Loan Approved ✅" if result[0] == 1 else "Loan Rejected ❌"

    return render_template("index.html", prediction=output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
