#import requests as rq
import torch
from transformers import pipeline
import os
from llm import llama_160m
os.environ["TRANSFORMERS_NO_TF"] = "1"


#sample audio file
"""url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3'
response = rq.get(url)
audio_file_path = "sample_audio.mp3"

if response.status_code == 200:
    with open(audio_file_path, 'wb') as file:
        file.write(response.content)
    print('file downloaded successfully')
else:
    print('failed to downlaod the file')"""

def transcript_audio(audio_file : str) -> str:
    pipe = pipeline(
        'automatic-speech-recognition',
        model='openai/whisper-tiny.en',
        chunk_length_s=30,
        framework="pt"
    )
    prediction = pipe(audio_file, batch_size = 8)['text']
    return llama_160m(prediction)