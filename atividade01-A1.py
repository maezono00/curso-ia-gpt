#Missão A — Receita personalizada: Peça pra IA criar uma receita de jantar para você.

import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

#O AGENTE É FEITO EM TUPLA POIS OS PARÂMETROS NÃO SERÃO ALERADOS.
agente = Agent (
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = "Escreva como você falaria com um amigo. Sem pensar muito.",
    tools = [DuckDuckGoTools(), WikipediaTools()],
    markdown = True
)

st.title("Missão A — Receita personalizada 🧑‍🍳")

pergunta = st.chat_input("Pergunte alguma coisa: ")

if pergunta:
    #O WITH SERVE PARA INICIAR UMA FUNÇÃO E ENCERRAR A MESMA ASSIM QUE CONCLUÍDA.
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        #O RESPOSTA.CONTENT SERVE PRA EXTRAIR SOMENTE A RESPOSTA EM SI GERADA PELO CHAT, GERALMENTE O CHATGPT GERA ID, PERGUNTA, TOKENS GASTOS, ETC...
        st.markdown(resposta.content)