import json
import ollama

with open("persony/nauczyciele/matematyka.json", "r") as f:
    dane = json.load(f)

historia = [
    {"role": "system", "content": dane["prompt"]}
]

def zapytanie(user_prompt):
    historia.append({"role": "user", "content": user_prompt})
    
    odpowiedz = ollama.chat(
        model="qwen3.5:9b",
        messages=historia,
        options={"num_predict": 8192, "num_ctx": 8192},
        think=False
    )
    
    wynik = odpowiedz["message"]["content"]
    historia.append({"role": "assistant", "content": wynik})
    print(wynik)
    return wynik