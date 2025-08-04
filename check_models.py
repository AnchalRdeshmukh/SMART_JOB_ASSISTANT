import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

print("Available Models:")
for model in models:
    print(f"- {model.name} → {model.supported_generation_methods}")
