from google import genai
import os
from dotenv import load_dotenv
import json

with open("persony/nauczyciele/matematyka.json", "r") as f:
    dane = json.load(f)

load_dotenv()
klucz = os.getenv("GEMINI_API")
gemini = genai.Client(api_key = klucz)

czat = gemini.chats.create(
    model="gemini-2.5-flash",
    config={"system_instruction": dane["prompt"]}
)


def onizuka(user_prompt):

    response = czat.send_message(user_prompt)
    return response.text
