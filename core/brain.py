import ollama



def klasyfikacja(user_prompt):
    odpowiedz = ollama.chat(
    model="qwen3.5:9b",
    options={"num_predict": 20, "num_ctx": 8192},
    think=False,
    messages=[
        {"role": "system", "content": "You are a text classifier. You will receive a message and you must return ONLY one word from the provided list of categories:'greeting, question, exercise, answer, other', and absolutely nothing else."},
        {"role": "user", "content": user_prompt}]
    )
    wynik = odpowiedz["message"]["content"]
    return wynik
def zapytanie(user_prompt):
    
    odpowiedz = ollama.chat(
        model="qwen3.5:9b",
        messages=[{"role": "system", "content": "You are a task executor. Complete the given task precisely. Be concise. Output only the result"},
                 {"role": "user", "content": user_prompt}],
        options={"num_predict": 8192, "num_ctx": 8192},
        think=False
    )
    
    wynik = odpowiedz["message"]["content"]
    print(wynik)
    return wynik