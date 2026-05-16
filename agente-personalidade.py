from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = "Você é um técnico de informática, seu modo de escrita é direta, porém, usa vários emoticons. Sua especialidade é em montagem e manutenções de computadores ou aparelhos de informática.",
    markdown = True
)

while True:
    pergunta = input("Insira texto: ")
    if (pergunta.lower() in ['sair', 'exit', 'não']):
        break
    else:
        agente.print_response(pergunta)