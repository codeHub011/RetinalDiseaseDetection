#Deep Feature Fusion-Based Retinal Eye Disease Detection from OCT Images
📌 Overview

This project presents a deep learning-based web application for automated detection of retinal diseases using OCT (Optical Coherence Tomography) images.

The system leverages a trained neural network model to classify retinal scans into multiple disease categories, enabling faster and more accurate diagnosis support.

🎯Key Features
🔍 Automated disease classification from OCT images
⚡ Fast and user-friendly web interface (Streamlit)
🧠 Deep learning model trained on large dataset (~84K images)
📊 Multi-class classification with high accuracy
💻 Works locally (no internet required after setup)
🩺 Disease Categories

The model classifies OCT images into the following classes:

CNV – Choroidal Neovascularization
DME – Diabetic Macular Edema
DRUSEN
NORMAL – Healthy retina

🛠️ Tech Stack
Programming Language: Python
Frameworks/Libraries:
TensorFlow / Keras
NumPy
Streamlit
Model Architecture: MobileNetV3 (for preprocessing & feature extraction)

📁 Project Structure
Project/
│── app.py
│── training_model.ipynb
│── Trained_eye_disease_model.h5
│── README.md

📊## Dataset
Source: Kaggle OCT Dataset
Size: ~84,000 images
Link: https://www.kaggle.com/datasets/anirudhcv/labeled-optical-coherence-tomography-oct
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-link>
cd project
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate
3️⃣ Install Dependencies
pip install streamlit tensorflow numpy

🚀How to Run
Step 1: Ensure Model File

Make sure:

Trained_eye_disease_model.h5

is present in the root directory.

Step 2: Start Application
streamlit run app.py
Step 3: Open in Browser
http://localhost:8501

🧑‍💻Usage Guide
Open the web application
Navigate to Disease Identification
Upload an OCT image
Click Predict
View classification result

🧠 Model Training Pipeline
Data collection and loading
Image preprocessing (resize to 224×224)
Train-test split
Model building using CNN architecture
Training & validation
Performance evaluation
Model saving (.h5)

📈Possible Improvements
🔬 Add more advanced architectures (EfficientNet, Vision Transformers)
📊 Include model performance metrics (Accuracy, Precision, Recall, F1-score)
🌐 Deploy on cloud (AWS / Azure / Streamlit Cloud)
🖼️ Add Grad-CAM visualization for explainability
📱 Make mobile-friendly UI
