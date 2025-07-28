from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import google.generativeai as genai  
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

# Load the trained model
model = tf.keras.models.load_model("leaf_classification_model.h5")

# Load medicinal properties CSV
df = pd.read_csv("Book1.csv")  # Update the CSV file name

# Class labels
class_names = [
    'Aloevera', 'Amla', 'Amruthaballi', 'Arali', 'Astma_weed', 'Badipala', 'Balloon_Vine', 'Bamboo', 'Beans', 
    'Betel', 'Bhrami', 'Bringaraja', 'Caricature', 'Castor', 'Catharanthus', 'Chakte', 'Chilly', 
    'Citron lime (herelikai)', 'Coffee', 'Common rue(naagdalli)', 'Coriender', 'Curry', 'Doddpathre', 'Drumstick', 
    'Ekka', 'Eucalyptus', 'Ganigale', 'Ganike', 'Gasagase', 'Ginger', 'Globe Amarnath', 'Guava', 'Henna', 'Hibiscus', 
    'Honge', 'Insulin', 'Jackfruit', 'Jasmine', 'Kambajala', 'Kasambruga', 'Kohlrabi', 'Lantana', 'Malabar_Nut', 
    'Malabar_Spinach', 'Mango', 'Marigold', 'Mint', 'Neem', 'Nelavembu', 'Nerale', 'Nooni', 'Onion', 'Padri', 
    'Palak(Spinach)', 'Papaya', 'Parijatha', 'Pea', 'Pepper', 'Pomoegranate', 'Pumpkin', 'Raddish', 'Rose', 
    'Sampige', 'Sapota', 'Seethaashoka', 'Seethapala', 'Spinach1', 'Tamarind', 'Taro', 'Tecoma', 'Thumbe', 'Tomato', 
    'Tulsi', 'Turmeric'
]

# Set up Gemini API
genai.configure(api_key="AIzaSyBTIhsX6j-3PlLcIgdzr9fMxlMLXuc6Me8")  

def get_ayurvedic_benefits(leaf_name):
    """Fetch Ayurvedic benefits from Gemini AI dynamically."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"What are the Ayurvedic benefits of {leaf_name}?"
        response = model.generate_content(prompt)
        return response.text.strip() if response else "No data available."
    except Exception as e:
        return f"Error fetching benefits: {str(e)}"

def get_medicinal_properties(leaf_name):
    """Retrieve medicinal properties from the CSV."""
    properties = df[df["Leaf Name"] == leaf_name].to_dict(orient="records")
    if not properties:
        return "No medicinal properties found."

    # Extract only properties marked as 1
    selected_properties = [key for key, value in properties[0].items() if value == 1 and key != "Leaf Name"]
    
    return ", ".join(selected_properties) if selected_properties else "No significant medicinal benefits."

def preprocess_image(image):
    """Preprocess image for model input."""
    image = image.resize((224, 224))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    try:
        image = Image.open(file)
        processed_image = preprocess_image(image)

        prediction = model.predict(processed_image)
        class_index = np.argmax(prediction)
        leaf_name = class_names[class_index]

        # Get medicinal properties
        medicinal_properties = get_medicinal_properties(leaf_name)

        # Fetch Ayurvedic benefits dynamically
        benefits = get_ayurvedic_benefits(leaf_name)

        return jsonify({
            "leaf_name": leaf_name,
            "medicinal_properties": medicinal_properties,
            "ayurvedic_benefits": benefits
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)  
