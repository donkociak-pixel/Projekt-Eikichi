from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
klucz = os.getenv("GEMINI_API")
gemini = genai.Client(api_key = klucz)



for m in gemini.models.list():
    print(m.name)