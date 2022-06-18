from _version import __version__
from flask import Flask
from flask import request
from flask.json import jsonify
import json
import pickle
import urllib.request

def get_model_date():
    url = urllib.request.urlopen("https://api.github.com/repos/barbaragribeiro/cloudcomp-argocd-k8s-predictor/commits?path=ml-model%2Fmodel.pickle&page=1&per_page=1")
    encoding = url.info().get_content_charset('utf-8')
    data = json.loads(url.read().decode(encoding))
    return data[0]['commit']['committer']['date']

def get_model():
    urllib.request.urlretrieve("https://github.com/barbaragribeiro/cloudcomp-argocd-k8s-predictor/raw/main/ml-model/model.pickle", "model.pickle")
    return pickle.load(open("model.pickle", "rb"))

app = Flask(__name__)
app._clf_pipeline = get_model()
app._version = __version__
app._model_date = get_model_date()

@app.route("/api/american", methods=["POST"])
def predict():
    text = request.get_json(force=True)["text"]
    if not isinstance(text, list):
        text = [text]
        predicted = app._clf_pipeline.predict(text)[0]
    else:
        predicted = app._clf_pipeline.predict(text).tolist()

    return jsonify(
        is_american=predicted,
        version=app._version,
        model_date=app._model_date
    )

if __name__ == "__main__":
    port = 5005
    app.run(debug=True, host='0.0.0.0', port=port)
