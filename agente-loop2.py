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

pergunta = input("Insira texto: ")
while True:
    agente.print_response(pergunta)
    continuar = input("Precisa de ajuda em mais alguma coisa? ")
    # if continuar.lower() == "sair" or continuar.lower() == "não":
    if continuar.lower() in ['n', 'nao', 'ñ', 'não', 'sair','exit']:
        print("Entedido! Encerrando sessão. 🤓")
        break
    else:
        agente.print_response(continuar)