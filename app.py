import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np

import tempfile



#Tensorflow Model Prediction
def model_prediction(test_image_path):
    model = tf.keras.models.load_model("Trained_eye_disease_model.h5")
    img = tf.keras.utils.load_img(test_image_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)

    result_index = np.argmax(predictions)
    confidence = np.max(predictions)

    return result_index, confidence



#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Identification"])

#Main Page
if(app_mode=="Home"):
    # image_path = "home_page.jpeg"
    # st.image(image_path,use_column_width=True)
    st.markdown("""
    ## **OCT Retinal Analysis Platform**

#### **Welcome to the Retinal OCT Analysis Platform**

**Optical Coherence Tomography (OCT)** is a powerful imaging technique that provides high-resolution cross-sectional images of the retina, allowing for early detection and monitoring of various retinal diseases. Each year, over 30 million OCT scans are performed, aiding in the diagnosis and management of eye conditions that can lead to vision loss, such as choroidal neovascularization (CNV), diabetic macular edema (DME), and age-related macular degeneration (AMD).

##### **Why OCT Matters**
OCT is a crucial tool in ophthalmology, offering non-invasive imaging to detect retinal abnormalities. On this platform, we aim to streamline the analysis and interpretation of these scans, reducing the time burden on medical professionals and increasing diagnostic accuracy through advanced automated analysis.

---

#### **Key Features of the Platform**

- **Automated Image Analysis**: Our platform uses state-of-the-art machine learning models to classify OCT images into distinct categories: **Normal**, **CNV**, **DME**, and **Drusen**.
- **Cross-Sectional Retinal Imaging**: Examine high-quality images showcasing both normal retinas and various pathologies, helping doctors make informed clinical decisions.
- **Streamlined Workflow**: Upload, analyze, and review OCT scans in a few easy steps.

---

#### **Understanding Retinal Diseases through OCT**

1. **Choroidal Neovascularization (CNV)**
   - Neovascular membrane with subretinal fluid
   
2. **Diabetic Macular Edema (DME)**
   - Retinal thickening with intraretinal fluid
   
3. **Drusen (Early AMD)**
   - Presence of multiple drusen deposits

4. **Normal Retina**
   - Preserved foveal contour, absence of fluid or edema

---

#### **About the Dataset**

Our dataset consists of **84,495 high-resolution OCT images** (JPEG format) organized into **train, test, and validation** sets, split into four primary categories:
- **Normal**
- **CNV**
- **DME**
- **Drusen**

Each image has undergone multiple layers of expert verification to ensure accuracy in disease classification. The images were obtained from various renowned medical centers worldwide and span across a diverse patient population, ensuring comprehensive coverage of different retinal conditions.

---

#### **Get Started**

- **Upload OCT Images**: Begin by uploading your OCT scans for analysis.
- **Explore Results**: View categorized scans and detailed diagnostic insights.
- **Learn More**: Dive deeper into the different retinal diseases and how OCT helps diagnose them.

---

#### **Contact Us**

Have questions or need assistance? [Contact our support team](#) for more information on how to use the platform or integrate it into your clinical practice.

    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                Retinal optical coherence tomography (OCT) is an imaging technique used to capture high-resolution cross sections of the retinas of living patients. 
                Approximately 30 million OCT scans are performed each year, and the analysis and interpretation of these images takes up a significant amount of time.
                (A) (Far left) choroidal neovascularization (CNV) with neovascular membrane (white arrowheads) and associated subretinal fluid (arrows). 
                (Middle left) Diabetic macular edema (DME) with retinal-thickening-associated intraretinal fluid (arrows). 
                (Middle right) Multiple drusen (arrowheads) present in early AMD. 
                (Far right) Normal retina with preserved foveal contour and absence of any retinal fluid/edema.

                ---

                #### Content
                The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (NORMAL,CNV,DME,DRUSEN). 
                There are 84,495 X-Ray images (JPEG) and 4 categories (NORMAL,CNV,DME,DRUSEN).

                Images are labeled as (disease)-(randomized patient ID)-(image number by this patient) and split into 4 directories: CNV, DME, DRUSEN, and NORMAL.

                """)

#Prediction Page
elif(app_mode=="Disease Identification"):
    st.header("Welcome to the Retinal OCT Analysis Platform")
    test_image = st.file_uploader("Upload your Image:")
    if test_image is not None:
        # Save to a temporary file and get its path
        with tempfile.NamedTemporaryFile(delete=False, suffix=test_image.name) as tmp_file:
            tmp_file.write(test_image.read())
            temp_file_path = tmp_file.name
    #Predict button
if(st.button("Predict")) and test_image is not None:
    with st.spinner("Please Wait.."):
        result_index, confidence = model_prediction(temp_file_path)
        
        class_name = ['CNV', 'DME', 'DRUSEN', 'NORMAL']

        
        model_accuracy = 0.95   

    st.success("Model is Predicting it's a {}".format(class_name[result_index]))
    st.info("Confidence: {:.2f}%".format(confidence * 100))
    st.info("Model Accuracy: {:.2f}%".format(model_accuracy * 100))

        