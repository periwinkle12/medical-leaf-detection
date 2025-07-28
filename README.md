# Ayurvedic Leaf Detection and Classification

This project uses deep learning to detect and classify Ayurvedic medicinal plant leaves based on uploaded images. It leverages a pre-trained MobileNet model and provides a user-friendly interface via Streamlit.

---

## 🧠 Features

- 📷 Upload and classify images of plant leaves
- 🔍 Predicts the plant type and its medicinal benefits
- 🧪 Trained using MobileNet for fast and lightweight inference
- 🧾 Simple UI built using Streamlit
- 🐳 Docker-ready setup for easy deployment

---

## 📁 Project Structure

.
├── .git/                         # Git configuration folder
├── .gitignore                    # Ignored files/folders
├── myenv/                        # Python virtual environment (should be in .gitignore)
├── app.py                        # Backend script (if used with Flask)
├── streamlit_app.py              # Streamlit UI script
├── Book1.csv                     # CSV file mapping leaf names to their benefits
├── Dockerfile                    # Docker configuration file
├── keras_metadata.pb             # Keras model metadata
├── leaf_benifit.ipynb            # Jupyter Notebook for leaf benefit prediction
├── leaf_classification_model.h5  # Trained model for classifying leaves
├── leaf_properties_model.h5      # Model for predicting medicinal properties
├── model.png                     # Model architecture diagram
├── requirements.txt              # Python dependencies
├── saved_model.pb                # Saved TensorFlow model
├── variables.index               # TensorFlow model variable index

🧾 Dataset
The dataset includes images of various Ayurvedic leaves along with their medicinal properties.

Source: (You can mention your source or say "custom-curated dataset")

📊 Model
CNN-based MobileNetV2 for leaf classification.

A separate model for predicting medicinal properties from classification output.

Training was done using Keras and TensorFlow.

🐳 Run with Docker
# Step 1: Clone the repository
git clone https://github.com/Kiran Behera/medical-leaf-detection.git
cd medical-leaf-detection

# Step 2: Build the Docker image
docker build -t leaf-detector .

# Step 3: Run the container
docker run -p 8501:8501 leaf-detector



