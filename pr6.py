from langchain_community.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from serpapi import GoogleSearch
from dotenv import load_dotenv
load_dotenv()

## 🔑 CARGA DE VARIABLES .ENV
Api_key_GROK=os.getenv("GROK_API_KEY")
Api_key_Serapi=os.getenv("SERAPI")

## 🔥 MODELO GROQ LLAMA 3.1 8B
modelo = ChatOpenAI(
    model="llama-3.1-8b-instant",
    api_key=Api_key_GROK,
    base_url="https://api.groq.com/openai/v1"
)

## TOOL GOOGLE
def SearchGoogle(query):
    res = GoogleSearch({"q": query,"api_key": Api_key_Serapi})
    result = res.get_dict()
    return result.get("organic_results", [])

GoogleTool = Tool(
    name="GoogleSearch",
    description="Busca información en Google usando SerpAPI.",
    func=SearchGoogle
)

## PROMPT PARA QUE EL AGENTE PUEDA USAR LA TOOL
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un agente con acceso a herramientas y puedes decidir cuándo usarlas con personalidad tsundere."),
    ("human", "{input}"),
    ("assistant","{agent_scratchpad}")  
])

## CREACIÓN DEL AGENTE (aquí estaba tu problema)
agente = create_openai_functions_agent(
    llm=modelo,
    tools=[GoogleTool],
    prompt=prompt
)

executor = AgentExecutor(agent=agente, tools=[GoogleTool], verbose=True)

## PRUEBA
RESPUESTA = executor.invoke({"input":"¿Que es lanchain ?"})

print(RESPUESTA["output"])
