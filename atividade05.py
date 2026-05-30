#Atividade prática 05 - Criação de Multi-Agentes

import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade", ["Nutricionista", "Personal Trainer", "Psicólogo"])

descricao = {
    "Nutricionista": "Especialista em alimentação saudável, sugere receitas e refeições equilibradas",
    "Personal Trainer": "especialista em exercícios físicos, monta treinos e dá dicas de musculação e cardio",
    "Psicólogo": "especialista em bem-estar mental, dá dicas de gerenciamento de estresse e ansiedade"
}

agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = descricao[personalidade],
    tools = [DuckDuckGoTools(), WikipediaTools()],
    markdown = True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
if st.sidebar.button("Limpar conversas"):
    st.session_state.mensagem = []
    st.rerun()
 
st.title("Seja bem vindo à Clínica, como podemos te ajudar?")
    
pergunta = st.chat_input("Pergunte ao agente")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    st.session_state.mensagem.append({"role": "user", "content": pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("O agente está pensando..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
        
    st.session_state.mensagem.append({"role": "assistant", "content": resposta.content})