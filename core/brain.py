import json
import ollama

def zapytanie(user_prompt):
    with open("persony/nauczyciele/matematyka.json", "r") as f:
        dane = json.load(f)
    
    odpowiedz = ollama.chat(
        model="qwen3.5:9b",
        messages=[
            {"role": "system", "content": dane["prompt"]},
            {"role": "user", "content": user_prompt}
        ],
        options={"num_predict": 512},
        think=False
    )
    wynik = odpowiedz["message"]["content"]
    print(wynik)
    return wynik