
# TODO: import your module
import requests
import os
import sys
from send_to_openai import speech_analyze_image

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = os.path.join(script_dir, "../frontend/src/downloaded_image.jpg")
mp3_filename = os.path.join(script_dir, "../frontend/src/image_analysis.mp3")
url = "http://172.20.10.6/1024x768.jpg"             # You will have to change the IP Address

# Function to download the image from esp32, given to you
def download_image(filename: str):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved to: {filename}")
    else:
        print("Failed to download image. Status code:", response.status_code)

# TODO: Download the image and get a response from openai
download_image(image_filename)
speech_analyze_image(image_filename,  "Analyze the image and look for clues.", mp3_filename, "Speak like a detective.")
