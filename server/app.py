from _version import __version__
from flask import Flask
from flask import request
from flask.json import jsonify
import pickle
import time
import os

model_file = "ml-model/model.pickle"

app = Flask(__name__)
app._clf_pipeline = pickle.load(open(model_file, "rb"))
app._version = __version__
app._model_date = time.ctime(os.path.getmtime(model_file))

@app.route("/api/american", methods=["POST"])
def predict():
    text = request.get_json(force=True)["text"]
    if not isinstance(text, list):
        text = [text]
    predicted = app._clf_pipeline.predict(text)

    return jsonify(
        is_american=predicted.tolist(),
        version=app._version,
        model_date=app._model_date
    )

if __name__ == "__main__":
    port = 5005
    app.run(debug=True, host='0.0.0.0', port=port)
