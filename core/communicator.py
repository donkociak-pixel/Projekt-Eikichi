from google import genai
import os
from dotenv import load_dotenv
import json


with open("persony/nauczyciele/matematyka.json", "r") as f:
    dane = json.load(f)

load_dotenv()
klucz = os.getenv("GEMINI_API")
gemini = genai.Client(api_key = klucz)
def onizuka(user_prompt):

    response = gemini.models.generate_content(
        model="gemini-2.5-flash-lite", contents = user_prompt)
    print(response.text)
