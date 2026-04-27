import pdfplumber
import os


def ekstraktor(sciezka_pliku):
    with pdfplumber.open(sciezka_pliku) as plik:
        liczba_stron = len(plik.pages)
        dane_wyjsciowe = []
        for numer_strony ,strona in enumerate(plik.pages):
            zawartosc = strona.extract_text()
            if zawartosc == None:
                continue
            slownik = {"tekst": zawartosc, "metadata": {"source": sciezka_pliku, "page": numer_strony}}
            dane_wyjsciowe.append(slownik)
    return dane_wyjsciowe
