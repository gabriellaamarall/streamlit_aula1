import streamlit as st

st.title("🚌 Expresso Mobilidade")

st.header("Painel do Operador")

st.write(
    "Bem-vindo ao painel operacional da Expresso Mobilidade. "
    "Aqui você pode consultar linhas e simular a distribuição de frota."
)

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}! Bom trabalho na operação de hoje.")

st.subheader("Consulta de Rotas")

linha = st.selectbox(
    "Escolha uma linha prioritária:",
    ["510", "520", "550"]
)

st.write("Linha selecionada:", linha)

st.subheader("Relatório de Linhas")

linhas = st.multiselect(
    "Escolha as linhas para o relatório:",
    ["510", "520", "550", "620"]
)

if linhas:
    st.write("Linhas selecionadas:", linhas)
else:
    st.info("Selecione uma ou mais linhas para gerar o relatório.")

st.subheader("Operações")

if st.button("Calcular demanda e frota"):
    if linhas:
        st.success(
            f"Cálculo realizado para {len(linhas)} linha(s) selecionada(s)."
        )
        st.write("Demanda analisada e distribuição de frota simulada.")
    else:
        st.warning("Selecione pelo menos uma linha antes de calcular.")