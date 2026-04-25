from core.brain import zapytanie
from core.communicator import onizuka


while True:
    user_prompt = input()
    if user_prompt == "exit":
        exit()
    onizuka(user_prompt)
