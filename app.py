from core.brain import zapytanie, klasyfikacja
from core.communicator import onizuka


while True:
    user_prompt = input()
    if user_prompt == "exit":
        exit()
    kategoria = klasyfikacja(user_prompt)
    print(f"{kategoria}")
    if kategoria == "greeting" or kategoria == "question" or kategoria == "exercise" or kategoria == "answer" or kategoria == "other":
        odpowiedz = onizuka(user_prompt)
        print(odpowiedz)
       
