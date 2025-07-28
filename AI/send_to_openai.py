# TODO: Import your libaries
import base64
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# TODO: Maybe you need a key?
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
if not OPENAI_API_KEY:
    raise ValueError("No API key found.")

client = OpenAI(api_key=OPENAI_API_KEY)

# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode('utf-8')


# TODO: Sending a request and getting a response

def analyze_image(image_path: str, prompt: str):
    """
    Analyzes an image according to the prompt and returns the analysis as a string.
    
    Args:
        image_path (str): path to the image to analyze.
        prompt (str): the prompt used to analyze the image.
    Returns:
        (Response): The analysis of the image.    
    """
    base64_image = encode_image(image_path)

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "what's in this image?" },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )
    print(response.output_text)
    return response


# TODO: How do we make things audible?

def text_to_speech(text: str, mp3_output_path: str, speech_instructions: str):
    """
    Convert a text to speech
    Args:
        text (str): the text to transcribe.
        mp3_output_path (str): The path to output the transcription.
        instructions (str): The instructions used to transcribe the text.
    """

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="ash",
        input=text,
        instructions=speech_instructions,
    ) as response:
        response.stream_to_file(mp3_output_path)

# TODO: Can we put everything together?
def speech_analyze_image(image_path: str, image_prompt: str, mp3_output_path: str, speech_prompt: str):
    print(f"Image prompt: {image_prompt}")

    text_analysis = analyze_image(image_path, image_prompt).output_text
    text_to_speech(text_analysis, mp3_output_path, speech_prompt)

if __name__ == '__main__':
    speech_analyze_image("image.jpg", "What is this an image of?", "test.mp3", "Speak like a knowlagible ")
