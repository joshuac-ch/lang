from langchain_community.tools import Tool
from langchain_openai import ChatOpenAI
from serpapi import GoogleSearch  # viene de google-search-results
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()
Api_key=os.getenv("GROK_API_KEY")
serApi_key=os.getenv("SERAPI")
modelo=ChatOpenAI(model="llama-3.1-8b-instant",api_key=Api_key,base_url="https://api.groq.com/openai/v1")
template=ChatPromptTemplate.from_messages([
    ("system","eres un asistente tsundere como nino nakano"),
    ("user","{pregunta}")
])
parser=StrOutputParser()
pipeline=RunnableSequence(template,modelo,parser)
def Search_Google(query):
    seach=GoogleSearch({
        "q":query,
        "api_key":  serApi_key
    })
    result=seach.get_dict()
    return result.get('organic_results',[])

Buscar=Tool(name="busqueda de google",description="funcion de busaqueda por internet",func=Search_Google)
res=Buscar.run("Que es un palindromo")

for item in res[:3]:
    print(item["title"], " - ",item.get('link'))


