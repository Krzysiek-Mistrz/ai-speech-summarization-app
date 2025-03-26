from transformers import pipeline
import gradio as gr
from stt import transcript_audio

def interface_launch():
    audio_input = gr.Audio(sources='upload', type='filepath')
    output_text = gr.Textbox()

    iface = gr.Interface(fn=transcript_audio, 
                        inputs=audio_input, 
                        outputs=output_text,
                        title='speech summarization app',
                        description='upload the audio file')

    iface.launch(server_name='0.0.0.0', server_port=7860)