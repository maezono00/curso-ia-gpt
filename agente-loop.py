from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#CARREGAR A CHAVE ANTES DE TUDO
load_dotenv()

#CRIAR MODELO DE IA
agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    markdown = True
)

while True:
    pergunta = input("Insira texto: ")
    if (pergunta.lower() == "sair" or "exit"):
        break
    else:
        agente.print_response(pergunta)