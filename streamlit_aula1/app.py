import streamlit as st
import pandas as pd

nome = "Gabriella"
idade = 17

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.write("Olá, mundo")

st.write("Meu nome é", nome, "e eu tenho", idade, "anos.")

st.title("Meu primeiro dash")
st.subheader(nome)

st.write(df)