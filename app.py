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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect',methods=['GET','POST'])
def detect():
    global COUNT
  
   
    base64_decoded = io.BytesIO(base64.b64decode(request.form['canvasimg'].split("base64",1)[1]))
    image_reshaped = prediction(base64_decoded)
    
    print(image_reshaped)

    # image = np.asarray(bytearray(base64_decoded), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # img.save('static/uploads/imgae_{}.jpg'.format(COUNT+1))
    state= 1
    
    return render_template('index.html', imgs =request.form['canvasimg'], state = state)
@app.route('/upload',methods=['GET','POST'])
def upload():
    img = request.files['imageTest']
    # print(img['FileStorage:'])
    image_reshaped = prediction(img)
    # imgs = img.resize((500, 500))
    # print(image_reshaped)
    state= 1
    return render_template('index.html',imgs =img, state = state)

if __name__ == '__main__':
    app.run()