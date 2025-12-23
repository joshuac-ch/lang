import os
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
apikey=os.getenv('GROK_API_KEY')
modelo=ChatOpenAI(model="llama-3.1-8b-instant",base_url="https://api.groq.com/openai/v1",api_key=apikey)

template=ChatPromptTemplate.from_messages([
    ("system","Eres un asistente inteligente con un caracter fuerte"),
    ("user","{pregunta}"),
    ("user","{historial}")])

parser=StrOutputParser()
pipeline=RunnableSequence(template,modelo,parser)
memoria=[]

def Memoria():
    if not memoria:
        return "no hay historial previo"
    texto=""
    for msg in memoria:
        texto+=f"{msg['role']}-{msg['content']}"
    return texto    

while True:
    pregunta=input("haga su pregunta: ")
    if(pregunta=="salir"):
        break
    historial=Memoria()
    respuesta=pipeline.invoke({"pregunta":pregunta,"historial":historial})
    print(respuesta)
    memoria.append({"role":"user","content":pregunta})
    memoria.append({"role":"assitent","content":respuesta})
