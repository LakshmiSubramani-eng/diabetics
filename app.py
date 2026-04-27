from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("disease_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
            float(data["pregnancies"]),
            float(data["glucose"]),
            float(data["bp"]),
            float(data["skin"]),
            float(data["insulin"]),
            float(data["bmi"]),
            float(data["dpf"]),
            float(data["age"])
    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        return jsonify({"result": "⚠️ High Risk of Diabetes"})
    else:
        return jsonify({"result": "✅ No Diabetes Detected"})

if __name__ == "__main__":
    app.run(debug=True)
