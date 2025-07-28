
# TODO: import your module
import requests
import os
import sys
from send_to_openai import speech_analyze_image


# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = os.path.join(script_dir, "../frontend/src/downloaded_image.jpg")
mp3_filename = os.path.join(script_dir, "../frontend/src/image_analysis.mp3")

# Function to download the image from esp32, given to you
# TODO: Download the image and get a response from openai
if __name__ == '__main__':
    prompt = sys.argv[1]
    print(prompt)
    speech_analyze_image(image_filename,  prompt, mp3_filename, "Speak like a detective.")
