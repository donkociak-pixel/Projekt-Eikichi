from google import genai
import os
from dotenv import load_dotenv
import json
import time
from datetime import datetime
with open("persony/nauczyciele/matematyka.json", "r") as f:
    dane = json.load(f)

load_dotenv()
klucz = os.getenv("GEMINI_API")
gemini = genai.Client(api_key = klucz)

czat = gemini.chats.create(
    model="gemini-3-flash-preview",
    config={"system_instruction": dane["prompt"],
            "thinking_config": {
                "include_thoughts": False,
                "thinking_budget": 2048
            }}
)


def onizuka(user_prompt):
    while True:
        czas = datetime.now().strftime("%H:%M:%S")
        try :
            response = czat.send_message(user_prompt)
            return response.text
        except KeyboardInterrupt:
            print("\n[!] Zatrzymano program ręcznie przez użytkownika (Ctrl+C).")
            exit()
        except Exception as e:
            print(f"{czas}, Ups, wystąpił błąd. Szczegóły: {e}")
            time.sleep(5)
