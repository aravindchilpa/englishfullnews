import nltk
import os

# Define the directory to store NLTK data
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')

# Ensure the directory exists
os.makedirs(nltk_data_dir, exist_ok=True)

# Download the required NLTK data
nltk.download('punkt', download_dir=nltk_data_dir)
