import numpy as np
from PIL import Image
import io
from tensorflow.keras.models import  load_model


model_ = load_model('Model_mnist.h5')
def prediction(image):
    img = Image.open(image).convert('L')
    img = img.resize((28, 28))
    image_np = np.array(img, order='C')
    image_reshaped = image_np.reshape(((28, 28, 1)))
    resultat = model_.predict([image_reshaped])
    print(resultat)
    return resultat