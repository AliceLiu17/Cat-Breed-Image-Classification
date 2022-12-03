import os
import pickle

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from sklearn import svm
from sklearn.model_selection import train_test_split

#helper function
def get_image(upload_file):
    st.image(Image.open(upload_file))
    img_array = np.array(Image.open(upload_file).convert('L').resize((150, 150))).reshape(1, 150*150)
    return img_array

def get_image_type(model, uploaded_file):
    img_array = get_image(uploaded_file)
    return model.predict(img_array)[0]


# app:
st.set_page_config(
    page_title= "Cat Breed Image Classification Demo",
    page_icon= "random",
    menu_items= {
        "Get Help": "https://github.com/AliceLiu17/Cat-Breed-Image-Classification",
        "Report a bug": "https://github.com/AliceLiu17/Cat-Breed-Image-Classification/issues/new",
        "About": """ **APPLICATION:** Provides cat breed prediction based on image classification"""
    }
)

c1, c2, c3 = st.columns([1, 6, 1])
with c2:
    st.title("Cat Breed Image Classifier")
    upload_file = st.file_uploader("")
    upload_file1 = st.file_uploader("Another image 1")
    upload_file2 = st.file_uploader("Another image 2")
    upload_file3 = st.file_uploader("Another image 3")

    if upload_file and upload_file1 and upload_file2 and upload_file3 is not None:
        # ML model
        svm_model = pickle.load(open("svm_model.pkl", "rb"))

        # results
        image_type = get_image_type(svm_model, upload_file)
        image_type1 = get_image_type(svm_model, upload_file1)
        image_type2 = get_image_type(svm_model, upload_file2)
        image_type3 = get_image_type(svm_model, upload_file3)
        
        if image_type == "bombay" :
            st.header(f"The cat is a {image_type}")
        elif image_type == "siamese":
            st.header(f"The cat is a {image_type}")
        elif image_type == "tabby":
            st.header(f"The cat is a {image_type}")
        else:
            st.header(f"Sorry, our model isn't trained on that cat!")

    else:
        st.info(f"""Upload a .JPG file please!""")
        st.stop()

        

