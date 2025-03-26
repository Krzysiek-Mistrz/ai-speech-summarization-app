from openai import OpenAI

def llama_160m(content : str) -> str:
    client = OpenAI(
        base_url="https://router.huggingface.co/hf-inference/models/Felladrin/Llama-160M-Chat-v1/v1",
        api_key="YOUR API HUGGING FACE KEY"
    )
    completion = client.chat.completions.create(
        model="Felladrin/Llama-160M-Chat-v1",
        messages=[
            {
                "role": "user",
                "content": f"provide a summary of this text: {content[:400]}"
            }
        ],
        max_tokens=500,
    )

    return completion.choices[0].message.content