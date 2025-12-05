from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_openai_functions_agent
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser  
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os 

load_dotenv()
ApyKeyGoogle=os.getenv("SERAPI")
ApyKeyGrok=os.getenv("GROK_API_KEY")

modelo=ChatOpenAI(model="llama-3.1-8b-instant",api_key=ApyKeyGrok,base_url="https://api.groq.com/openai/v1")

template=ChatPromptTemplate.from_messages([
    ("system","eres un asistente virtual"),
    ("human","{pregunta}"),
    ("assistant","{agent_scratchpad}")
])
parser=StrOutputParser()

def SearhGoo(query):
    res=GoogleSearch({"q":query,"api_key":ApyKeyGoogle})
    result=res.get_dict()
    return result.get("organic_results",[]) 

GoogleTool=Tool(name="SearchGoogle",description="Buscar en google informacion",func=SearhGoo)

agente=create_openai_functions_agent(llm=modelo,tools=[GoogleTool],prompt=template)

ejecutor=AgentExecutor(agent=agente,tools=[GoogleTool], verbose=True)
res=ejecutor.invoke({"pregunta":"que es DDOS"})
print(res["output"])