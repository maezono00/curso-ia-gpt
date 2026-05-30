import streamlit as st

st.title("Secretaria SENAI Americana")
st.subheader("Conheça os nossos cursos!")

st.write("I.A Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador.")
st.markdown("**ATENÇÃO**: Verifique se existem vagas disponíveis.")

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite a sua idade: ", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos disponíveis", ["I.A Generativa", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui, você aceita os termos e condições.")

if st.button("Enviar resposta"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Parabéns, {nome}! Você concluiu a inscrição para o curso de {cursoEscolhido} e a sua idade ({idade} anos) está dentro do requisitos mínimos.")
    else:
        st.error("Dados inseridos incorretamente.")