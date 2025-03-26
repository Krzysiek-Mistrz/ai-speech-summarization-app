# Speech Summarization App  

A web application built in Python that takes an audio file as input, transcribes it using **Whisper Tiny** (STT), and then summarizes the resulting text using a LLM **(Llama-160M)**. The app is packaged and ready for deployment, featuring a simple Gradio interface for ease of use.  

## Features  

- **Audio Upload:** Allows users to upload an audio file directly from the browser.   
- **Speech-to-Text (STT):** Uses OpenAI's Whisper Tiny model for converting speech to text.  
- **Text Summarization:** Employs the Llama-160M Chat model via Hugging Face's inference API to generate a concise summary of the transcribed text.  
- **Web Interface:** Built using Gradio for a user-friendly and interactive experience.  

## Installation  

1. **Clone the Repository:**  
```bash  
git clone https://github.com/yourusername/speech-summarization-app.git  
cd speech-summarization-app  
```

2. **Other modules:**  
You also need:  
- transformers  
- gradio  
- torch  
- openai  

3) **API KEY**
You need to have account on hugging facve and create read type api key and type it into: `api_key="YOUR API HUGGING FACE KEY"` in `llm.py`  

## Usage  
To start the application, simply run:  
```bash
python app.py
```  
You can also use this project as a separate package and just `import app` and use `interface_launch()` function to launch the whole interface. You can change everything under apache lic. Cheers ;)