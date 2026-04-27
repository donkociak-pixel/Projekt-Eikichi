import pdfplumber
import os


def konwersja(sciezka_pliku):
    plik_wiedza=pdfplumber.open(sciezka_pliku)
    text=""
    for strona in plik_wiedza:
        zawartosc = strona.extract_text()
        if zawartosc == None:
            continue
        text = text + zawartosc
