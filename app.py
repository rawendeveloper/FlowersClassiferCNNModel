import os 
import keras
from keras.models import load_model 
import streamlit as st
import tensorflow as tf
import numpy as np

st.header('Flower Classification CNN Model')

flower_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

model = load_model('Flower_recog_Model.h5')

def classify_images(image_path):
    # Load the image
    input_image = tf.keras.utils.load_img(image_path, target_size=(180, 180))
    input_image_array = tf.keras.utils.img_to_array(input_image)

    # Expand dimensions to fit model input
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)  # Make sure to specify the axis

    # Make predictions
    predictions = model.predict(input_image_exp_dim)

    result = tf.nn.softmax(predictions[0])
    outcome = 'The image belongs to ' + flower_names[np.argmax(result)] + ' with a score of ' + f'{np.max(result) * 100:.2f}%'
    return outcome

uploaded_file = st.file_uploader('Upload an Image')

if uploaded_file is not None:
    # Ensure the 'upload' directory exists
    if not os.path.exists('upload'):
        os.makedirs('upload')
    
    file_path = os.path.join('upload', uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Display the uploaded image
    st.image(file_path, caption='Uploaded Image', use_column_width=True)

    # Classify the image and display the result
    result = classify_images(file_path)
    st.write(result)
