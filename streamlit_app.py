import streamlit as st
import requests
from PIL import Image
import io

# Streamlit App Title
st.title("🍃 Leaf Identification & Ayurvedic Benefits")

# File uploader for leaf image
uploaded_file = st.file_uploader("📤 Upload an image of a leaf", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Leaf", use_column_width=True)

    if st.button("🔍 Identify Leaf"):
        with st.spinner("Processing... ⏳"):
            try:
                # Convert image to bytes
                image_bytes = io.BytesIO()
                image.save(image_bytes, format="JPEG")
                image_bytes = image_bytes.getvalue()

                # Send request to Flask API
                files = {"file": ("leaf.jpg", image_bytes, "image/jpeg")}
                response = requests.post("http://127.0.0.1:5001/predict", files=files)

                # Handle response
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display the identified leaf name
                    st.success(f"🌿 Identified Leaf: **{data['leaf_name']}**")

                    # Display medicinal properties (if available)
                    if data["medicinal_properties"] != "No significant medicinal benefits.":
                        st.markdown(f"💊 **Medicinal Properties:**\n\n `{data['medicinal_properties']}`")
                    else:
                        st.warning("⚠️ No major medicinal properties found for this leaf.")

                    # Display Ayurvedic benefits
                    st.markdown(f"📜 **Ayurvedic Benefits:**\n\n {data['ayurvedic_benefits']}")

                else:
                    st.error("❌ Error in prediction. Please try again.")

            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
