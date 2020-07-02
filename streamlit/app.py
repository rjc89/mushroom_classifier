# https://www.pluralsight.com/guides/deploying-image-classification-on-the-web-with-streamlit-and-heroku
import streamlit as st
from img_classification import teachable_machine_classification

st.title("Prototype Mushroom Classifier - Using Transfer Learning With mobilenet_V2")
st.header('Mushroom Classifier')
st.text('Upload a mushroom image')

uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
    if label == 0:
        st.write("The MRI scan has a brain tumor")
    else:
        st.write("The MRI scan is healthy")

