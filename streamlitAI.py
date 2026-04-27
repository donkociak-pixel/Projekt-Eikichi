import streamlit as st
from core.brain import zapytanie, klasyfikacja
from core.communicator import onizuka

# 1. Konfiguracja strony
st.set_page_config(page_title="Onizuka AI - Matematyka", page_icon="🎓")
st.title("🎓 Onizuka-sensei: Matematyka")

# 2. Inicjalizacja historii czatu w pamięci sesji (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Wyświetlanie historii wiadomości z poprzednich kroków
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Pole wejściowe dla użytkownika (zamiast input())
if user_prompt := st.chat_input("Napisz do nauczyciela..."):
    
    # Dodaj wiadomość użytkownika do historii i wyświetl ją
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 5. Logika klasyfikacji i generowania odpowiedzi
    with st.spinner("Onizuka myśli..."):
        kategoria = klasyfikacja(user_prompt)
        
        # Opcjonalnie: wyświetl kategorię (np. w sidebarze lub jako mały tekst)
        st.caption(f"Wykryta kategoria: {kategoria}")

        if kategoria in ["greeting", "question", "exercise", "answer", "other"]:
            odpowiedz = onizuka(user_prompt)
            
            # Dodaj odpowiedź AI do historii i wyświetl ją
            st.session_state.messages.append({"role": "assistant", "content": odpowiedz})
            with st.chat_message("assistant"):
                st.markdown(odpowiedz)