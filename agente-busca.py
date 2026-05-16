#FERRAMENTA PARA QUE O AGENTE USE PESQUISA: duckduckgo-search, ddgs, tavily
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = "Você é um técnico de informática, seu modo de escrita é direta, porém, usa vários emoticons. Sua especialidade é em montagem e manutenções de computadores ou aparelhos de informática.",
    add_history_to_context = True,
    tools = [DuckDuckGoTools(), TavilyTools()],
    markdown = True
)

while True:
    pergunta = input("Insira texto: ")
    if (pergunta.lower() in ['sair', 'exit', 'não']):
        break
    else:
        agente.print_response(pergunta)