# https://towardsdatascience.com/image-classification-of-uploaded-files-using-streamlits-killer-new-feature-7dd6aa35fe0
import tensorflow as tf
import tensorflow_hub as hub
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16


from PIL import Image
import io
from io import BytesIO

def predict(image): 
    model = tf.keras.models.load_model('/home/robert/Downloads/Mushroom_classifier/streamlit/mushroom_model/keras')
    
    #image = '/home/robert/Downloads/Mushroom_classifier/streamlit/Boletus_edulis_steinpilz.jpg'
    image = '/home/robert/Downloads/Mushroom_classifier/streamlit/Laetiporus_sulphureus_JPG01.jpg'
    #model = VGG16()

    #image = Image.open(uploaded_file)

    image = load_img(image, target_size=(224, 224))

    #imgstr = image.read()
    #image = load_img(open(BytesIO(image)), target_size=(224, 224))
    #image = load_img(open(BytesIO(image)).read(), target_size=(224, 224))

    # convert the image pixels to a numpy array
    image = img_to_array(image)
    
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    
    # prepare the image for the VGG model
    image = preprocess_input(image)
    
    # predict the probability across all output classes
    #yhat = model.predict(image)
    yhat = model.predict(image)
    y_classes = yhat.argmax(axis=-1)
    # convert the probabilities to class labels
    #label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    #label = label[0][0]
    return yhat    #, y_classes 