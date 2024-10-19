# Sans titre

# 🌼 Flower Classification CNN Model 🌻

## 🌟 Overview

This project is a deep learning-based flower classification application built using a **Convolutional Neural Network (CNN)**. It can identify images of flowers belonging to the following categories:

- 🌼 **Daisy**
- 🌻 **Dandelion**
- 🌹 **Rose**
- 🌞 **Sunflower**
- 🌷 **Tulip**

The application utilizes **TensorFlow** and **Keras**, and is deployed with **Streamlit**, providing an intuitive and interactive web interface for users to upload an image and receive instant predictions.

---

## 📋 Table of Contents

- [Features](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [Getting Started](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
    - [Prerequisites](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
    - [Installation](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
    - [Usage](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [Model Architecture](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [Directory Structure](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [Future Enhancements](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [Contributing](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)
- [License](https://www.notion.so/124b6f04a80680ff976bd56443416577?pvs=21)

---

## ✨ Features

- **📁 Image Upload**: Upload a flower image directly through the web interface.
- **🌼 Image Classification**: The model processes the image and predicts the flower category, displaying the result along with the confidence score.
- **🖥️ User-Friendly Interface**: Simple and accessible for anyone interested in flower classification.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- TensorFlow 2.x
- Keras
- Streamlit
- Numpy

### Installation

Follow these steps to set up the project:

1. Clone this repository:
    
    ```bash
    
    git clone https://github.com/yourusername/flower-classification-cnn-model.git
    
    ```
    
2. Navigate to the project directory:
    
    ```bash
    
    cd flower-classification-cnn-model
    
    ```
    
3. Install the required dependencies:
    
    ```bash
    
    pip install -r requirements.txt
    
    ```
    

### Usage

1. Run the Streamlit application:
    
    ```bash
    
    Copier le code
    streamlit run app.py
    
    ```
    
2. Open the web application in your browser. You will see an interface where you can upload a flower image.
3. Upload the image, and the model will predict the flower type and display the classification result along with the confidence score.

---

## 🧠 Model Architecture

The CNN model has the following structure:

- **Data Augmentation**: Includes random flipping, rotation, and zoom to increase dataset variety.
- **Conv2D & MaxPooling Layers**: Convolutional and pooling layers to extract and downsample features.
- **Dropout Layer**: To reduce overfitting during training.
- **Dense Layers**: Fully connected layers for classification.

The model is trained on a popular Flowers dataset, which contains multiple images for each flower category, ensuring robust and accurate classification.

---

## 📁 Directory Structure

```bash
bash
Copier le code
flower-classification-cnn-model/
│
├── app.py                 # Main application file
├── Flower_recog_Model.h5  # Pre-trained model file
├── upload/                # Directory for storing uploaded images
├── requirements.txt       # Dependencies for the project
└── README.md              # This readme file

```

---

## 🔍 Example

1. Launch the application using Streamlit.
2. Upload an image of a flower (e.g., a sunflower).
3. The application will predict the flower type and display the probability score.

---

## 🌱 Future Enhancements

- 🏷️ **Add More Flower Types**: Expand the model to recognize additional flower types.
- ⚡ **Performance Optimization**: Optimize the model for faster inference and improved accuracy.
- ☁️ **Cloud Deployment**: Deploy the application using cloud services for increased accessibility.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙏 Acknowledgments

- Special thanks to **TensorFlow** and **Keras** for providing the tools to build and train the CNN model.
- **Streamlit** for simplifying the deployment process and creating an intuitive user interface.

---
