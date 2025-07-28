# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose both Flask and Streamlit ports
EXPOSE 5000
EXPOSE 8501

# Run both Flask and Streamlit together
CMD ["bash", "-c", "python app.py & streamlit run streamlit_app.py --server.port=8501 --server.enableCORS=false"]
