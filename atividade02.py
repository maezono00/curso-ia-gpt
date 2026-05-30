#
import streamlit as st

st.title("Bem vindo ao sistema de RH 2000!!! 👩‍💼")
st.subheader("Por favor, insira seus dados para efetuarmos o cadastro.")

nome = st.text_input("Por favor, insira seu nome completo: ")
email = st.text_input("Por favor, insira o seu email: ")

#A VERIFICAÇÃO SE OS DADOS FORAM PREENCHIDOS ADEQUADAMENTE SERÁ FEITA COM ESSE BOTÃO, CASO CONTRÁRIO, O PROGRAMA VAI ESTAR SEMPRE VERIFICANDO SE AS CAIXAS DE TEXTO ESTARÃO PREENCHIDAS, MESMO O CÓDIGO SENDO EXECUTADO PELA PRIMEIRA VEZ!
if st.button("Enviar dados"):
    if nome and email:
        st.success("Dados cadastrados com sucesso!!!")
        st.balloons()
    else:
        st.error("Dados incompletos. 👎")