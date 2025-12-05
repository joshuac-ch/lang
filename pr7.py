from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_openai_functions_agent
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser  
from dotenv import load_dotenv
import os 

load_dotenv()
ApyKeyGoogle=os.getenv("SERAPI")
ApyKeyGrok=os.getenv("GROK_API_KEY")

modelo=ChatOpenAI(model="llama-3.1-8b-instant",api_key=ApyKeyGrok,base_url="https://api.groq.com/openai/v1")

template=ChatPromptTemplate.from_messages([
    ("system","eres un asistente virtual"),
    ("user","{pregunta}")
])
parser=StrOutputParser()

pipeline=RunnableSequence(template,modelo,parser)

res=pipeline.invoke({"pregunta":"dame el abecedario completo"})
print(res)