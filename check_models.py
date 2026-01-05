import os
from dotenv import load_dotenv
from google import genai
from pathlib import Path

# Force load .env from project root
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")
print("API KEY FOUND:", bool(api_key))

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not loaded. Check .env file location.")

client = genai.Client(api_key=api_key)

models = client.models.list()

for m in models:
    print(m.name)


