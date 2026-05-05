
OCT Retinal Disease Detection System
This project is a Deep Learning-based Web Application that detects retinal diseases from OCT (Optical Coherence To■ Project Overview
The system classifies OCT images into the following categories:
- CNV (Choroidal Neovascularization)
- DME (Diabetic Macular Edema)
- DRUSEN
- NORMAL
It uses a trained model (Trained_eye_disease_model.h5) and provides a simple UI for users to upload images and ge■■ Technologies Used
- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- MobileNetV3 (for preprocessing)

  
■ Project Structure
Project/
- app.py
-  training_model.ipynb
- rained_eye_disease_model.h5
- README.md

  Dataset -> https://www.kaggle.com/datasets/anirudhcv/labeled-optical-coherence-tomography-oct
  
■■ Setup & Installation
1. Clone the Repository
git clone <your-repo-link>
cd project
2. Create Virtual Environment
python -m venv venv
Activate:
Windows → venv\Scripts\activate
Linux/Mac → source venv/bin/activate
3. Install Dependencies
pip install streamlit tensorflow numpy
■■ How to Run the Project
Step 1: Ensure Model File Exists
Trained_eye_disease_model.h5 must be present

Step 2: Run
streamlit run app.py

Step 3: Open
http://localhost:8501

■ How to Use
1. Open the web app
2. Go to Disease Identification
3. Upload an OCT image
4. Click Predict
5. View result
   
■ Model Training Process
- Dataset: ~84,000 images
- Classes: CNV, DME, DRUSEN, NORMAL
Steps:
1. Load dataset
2. Preprocess images
3. Split dataset
4. Build model
5. Train model
6. Evaluate performance
7. Save model (.h5)
   
■ Platforms Used
- VS Code
- Local Machine
- Streamlit Cloud
  
■■ Important Notes
- Image size: 224x224
- Model file required
- No internet needed after setup
■ Future Improvements
- Accuracy display
- Online deployment
- Better UI
- Multi-image support
- Streamlit Cloud
