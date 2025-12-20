from huggingface_hub import InferenceClient
import os
import sys
from dotenv import load_dotenv

load_dotenv()
hf_api_token = os.getenv("HF_API_TOKEN", "NAN")
hf_model = os.getenv("HF_MODEL", "NAN")

if hf_api_token == "NAN" or hf_model == "NAN":
    print("hf_api_token or hf_model missing from .env")
    print("make sure to have a valid .env from .env.example")
    sys.exit(1)

client = InferenceClient(model=hf_model, token=hf_api_token)

def query(user_prompt, history):
    messages = history
    messages.append({"role": "user", "content": user_prompt})
    response = client.chat_completion(messages)
    return response.choices[0].message.content
