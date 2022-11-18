
import numpy as np
from PIL import Image
import io
from tensorflow.keras.models import  load_model


model_ = load_model('Model_mnist.h5')
def prediction(image):
#     La fonction prediction comme son nom le dit permet de recuperer les entrer et de faire une detection de chiffre 
    img = Image.open(image).convert('L')
    img = img.resize((28, 28))
    image_np = np.array(img, order='C')
    image_reshaped = image_np.reshape(((1,28, 28)))
    resultat = model_.predict([image_reshaped])

    return np.argmax(resultat, axis=1):
