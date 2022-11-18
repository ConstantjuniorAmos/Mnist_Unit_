from flask import Flask,url_for,render_template, request
import re
import base64
from PIL import Image
import io
import numpy as np
from werkzeug.utils import secure_filename
from fonction import prediction




COUNT = 0
app = Flask(__name__)

app.config["SEND_FILE_MAX_AGE_DEFAULT"]=10
# La fonction index sert de porte d'entrée sur l'application
@app.route('/')
def index():
    return render_template('index.html')
# La fonction detect est appelé lors que l'utilisateur utilise le canva pour dessiner les chiffre
@app.route('/detect',methods=['GET','POST'])
def detect():
    global COUNT
  
   
    base64_decoded = io.BytesIO(base64.b64decode(request.form['canvasimg'].split("base64",1)[1]))
    image_reshaped = prediction(base64_decoded)
    state= 1
    
    return render_template('index.html', imgs =request.form['canvasimg'], state = state, predict = image_reshaped)
# cette fonction est utilisée lors que l'utilisateur upload une image
@app.route('/upload',methods=['GET','POST'])
def upload():
    img = request.files['imageTest']
    image_reshaped = prediction(img)
   
    state= 1
    return render_template('index.html',imgs =img, state = state,predict = image_reshaped)

if __name__ == '__main__':
    app.run()
