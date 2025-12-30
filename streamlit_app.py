import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import pandas as pd
import numpy as np

def genereaza_csv_istoric(nume_fisier="loto_real.csv", randuri=200):
    date = []
    for _ in range(randuri):
        # Generăm 6 numere unice între 1 și 49
        extragere = sorted(np.random.choice(range(1, 50), 6, replace=False))
        date.append(extragere)
    
    # Creăm DataFrame-ul cu numele coloanelor
    df = pd.DataFrame(date, columns=['n1', 'n2', 'n3', 'n4', 'n5', 'n6'])
    
    # Salvăm în format CSV
    df.to_csv(nume_fisier, index=False)
    print(f"Fișierul {nume_fisier} a fost generat cu succes cu {randuri} extrageri!")

# Apelăm funcția
genereaza_csv_istoric()
