from mimetypes import init
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

def query(prompt, history, role):
    messages = history
    if role == "user":
        messages.append({"role": "user", "content": f'{{"user_msg": "Give response in JSON only. {prompt}"}}'})
    elif role == "system":
        messages.append({"role": "system", "content": f"Give response in JSON only. {prompt}"})
    else:
        print(f"tried to query as role {role}")
        sys.exit(1)
    response = client.chat_completion(messages)
    return response.choices[0].message.content

# sample query
if __name__ == "__main__":
    from prompts import init_prompt
    print(query(init_prompt() + '{"user_msg": "can you give me the current weather?"}', [], "user"))
