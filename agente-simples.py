#INSTALAR, ALÉM DA BIBLIOTECA REQUESTS E O FRAMEWORK PYTHON-DOTENV, A BIBLIOTECA OPENAI E O FRAMEWORK AGNO
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#TODOS OS AGENTES NECESSITAM DA CHAVE DE API, CARREGAR A CHAVE USANDO A FUNÇÃO load_dotenv(). ELA SERÁ RESPONSÁVEL POR LER A CHAVE DENTRO DO .env.
load_dotenv()

agente = Agent(
    model = OpenAIChat(id="gpt-4o-mini"),
    markdown = True
)

agente.print_response("Receita de pão de ló")