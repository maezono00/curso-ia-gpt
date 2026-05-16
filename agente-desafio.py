from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

agente = Agent(
    model = OpenAIChat(id="gpt-4o-mini"),
    markdown = True
)

pergunta = input("Insira texto: ")
agente.print_response(pergunta)