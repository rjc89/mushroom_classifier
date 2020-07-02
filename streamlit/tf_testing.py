import tensorflow as tf
from keras.preprocessing.image import load_img
from PIL import Image

model = tf.keras.models.load_model('/home/robert/Downloads/Mushroom_classifier/streamlit/mushroom_model/keras')
image1 = '/home/robert/Downloads/RJC_profile.jpg'
image1 = Image.open(image1)
image = load_img(image1, target_size=(224, 224))
model.predict(image)


