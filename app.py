from core.brain import zapytanie



while True:
    user_prompt = input()
    if user_prompt == "exit":
        exit()
    zapytanie(user_prompt)
