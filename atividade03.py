import streamlit as st

with st.container(horizontal_alignment='center'):
    st.image("pizza.png")
st.title("Pesquisa de satisfação DiPadre Pizarria 🍕")
st.subheader("Conte para nós o que achou!")

nomeCliente = st.text_input("Insira o seu nome: ")
cidadeCliente = st.text_input("Insira a cidade que você mora: ")
bairroCliente = st.text_input("Insira o bairro que você mora: ")
saborCliente = st.selectbox("Selecione o sabor consumido: ", ["Calabresa", "Margherita", "Portuguesa", "Quatro Queijos"])
aceitarTermos = st.checkbox("Ao selecionar essa opção, você concorda com os termos e condições.")

if st.button("Enviar respostas"):
    if nomeCliente and cidadeCliente and bairroCliente and saborCliente and aceitarTermos:
        st.success(f"Obrigado, {nomeCliente} por responder a pesquisa!\nSegue as informações inseridas:\n Nome: {nomeCliente},\n Cidade: {cidadeCliente},\n Bairro: {bairroCliente}\n e Sabor escolhido: {saborCliente}")
        st.balloons()
    else:
        st.error("Dados incorretos.")