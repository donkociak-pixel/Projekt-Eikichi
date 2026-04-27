import chromadb
import os


def memory(dane_wejsciowe, nazwa_przedmiotu):
    client= chromadb.PersistentClient(path="./baza_wektorowa")
    kolekcja = client.create_collection(name = nazwa_przedmiotu)
    documents = []
    metadatas = []
    ids = [] 
    for i , element in enumerate(dane_wejsciowe):
        documents.append(element["tekst"])
        metadatas.append(element["metadata"])
        ids.append(f"id_{i}")
    kolekcja.add(documents, metadatas,ids)
    return True
