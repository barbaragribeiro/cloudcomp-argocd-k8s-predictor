from flask import Flask
from flask import request
from flask.json import jsonify
import pickle

app = Flask(__name__)
app._clf_pipeline = pickle.load(open("ml-model/model.pickle", "rb"))

@app.route("/api/american", methods=["POST"])
def predict():
    text = request.get_json(force=True)["text"]
    if not isinstance(text, list):
        text = [text]
    predicted = app._clf_pipeline.predict(text)
    return jsonify(predicted=predicted.tolist())

if __name__ == "__main__":
    port = 5005
    app.run(debug=True, host='0.0.0.0', port=port)
