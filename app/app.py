import base64
import io
import re

import numpy as np
from flask import Flask, jsonify, render_template, request
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("app/model/mnist.h5")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    encoded = data["image"]
    imgstr = re.search(r"base64,(.*)", encoded).group(1)
    decoded = base64.b64decode(imgstr)
    image = Image.open(io.BytesIO(decoded))
    # convert image to gray scale mode
    image = image.convert("L")
    image = image.resize((28, 28))
    image = np.array(image)
    # invert image
    image = 255 - image
    # normalize image
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)
    # make prediction with the model
    prediction = model.predict(image).reshape(-1)
    prob = prediction.tolist()
    prob = [format(num, ".4f") for num in prob]
    label = np.argmax(prob).tolist()
    confidence = prob[label]
    return jsonify({"prob": prob, "label": label, "confidence": confidence})


@app.route('/upload',methods=['GET','POST'])
def upload():
    img = request.files['imageTest']
    confidence, label, prob = prediction(img)
    # print(image_reshaped)
    return jsonify({"prob": prob, "label": label, "confidence": confidence})
   
    # state= 1
    # return render_template('index.html',imgs =img, state = state,predict = image_reshaped)

def prediction(image_):
#     La fonction prediction comme son nom le dit permet de recuperer les entrer et de faire une detection de chiffre 
    img = Image.open(image_).convert('L')
    img = img.resize((28, 28))
    image_np = np.array(img)
     # invert image
    image = 255 - image_np
    # normalize image
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)
    prediction = model.predict(image).reshape(-1)
    prob = prediction.tolist()
    prob = [format(num, ".4f") for num in prob]
    label = np.argmax(prob).tolist()
    confidence = prob[label]
    return confidence, label, prob

    # return np.argmax(resultat, axis=1)

if __name__ == "__main__":
    app.run()

