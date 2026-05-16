#FERRAMENTA PARA QUE O AGENTE USE PESQUISA: duckduckgo-search, ddgs, tavily
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
#BIBLIOTECA PARA MANIPULAR BANCO DE DADOS
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

bancoDados = SqliteDb(db_file="temp/registros.db")

agente = Agent(
    model = OpenAIChat(id = "gpt-4o-mini"),
    description = "Você é um técnico de informática, seu modo de escrita é direta, porém, usa vários emoticons. Sua especialidade é em montagem e manutenções de computadores ou aparelhos de informática.",
    add_history_to_context = True,
    db = bancoDados,
    #FORÇA O OPENIA A PUXAR OS DADOS COM BASE NO ID DA SESSÃO
    session_id="4b471813-b9af-4bac-a259-f586735d2f9f",
    num_history_runs=7,
    tools = [DuckDuckGoTools(), TavilyTools()],
    markdown = True
)

while True:
    pergunta = input("Insira texto: ")
    if (pergunta.lower() in ['sair', 'exit', 'não']):
        break
    else:
        agente.print_response(pergunta)