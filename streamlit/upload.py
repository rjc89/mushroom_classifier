# https://towardsdatascience.com/image-classification-of-uploaded-files-using-streamlits-killer-new-feature-7dd6aa35fe0
import streamlit as st 
from PIL import Image
import classify
from classify import predict

st.title("Mushroom Image Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predict(uploaded_file)
    label_dict = {'Agaricus': 0, 'Amanita': 1, 'Boletus': 2, 'Cantharellus': 3, 
    'Laetiporus': 4, 'Macrolepiota': 5, 'Pleurotus': 6}
    #st.write('%s (%.2f%%)' % (label[1], label[2]*100))
    
    for i, j in enumerate(label_dict):
        st.write(j, label[0][i])
   
