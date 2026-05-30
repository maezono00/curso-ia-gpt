#PARA TESTAR O CÓDIGO WEB É NECESSÁRIO EXECUTAR: streamlit run {nome do arquivo}.py

#IMPORTAR FRAMEWORK DE FRONTEND PRO CÓDIGO
#O FROM É: TRAGA UM COMPONENTE ESPECÍFICO DESSA CAIXA DE FERRAMENTAS

import streamlit as st #É POSSÍVEL TAMBÉM ATRIBUIR UM ALIAS PARA A BIBLIOTECA COM O "AS"

st.title("Bem vindo à minha primeira página web!!! 🤓")
st.subheader("Desenvolvido por: Arthur")

nome = st.text_input("Digite o seu nome: ")

if nome:
    st.success(f"Bem vindo, {nome}!!!")
    st.balloons()