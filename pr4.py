import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
APY_KEY_GROK=os.getenv("GROK_API_KEY")

modelo=ChatOpenAI(model="llama-3.1-8b-instant",api_key=APY_KEY_GROK,base_url="https://api.groq.com/openai/v1")
memoria=[]
template=ChatPromptTemplate.from_messages([
    ("system","Eres un asistente inteligente tsundere como nino nakano"),
    ("user","{pregunta}"),
    ("user","{memoria}")
])
parser=StrOutputParser()
pipeline=RunnableSequence(template,modelo,parser)

def Contruir_Memoria():
    if not memoria:
        return "No hay historial previo."
    texto=""
    for msg in memoria:
        texto+=f"{msg['role']}: {msg['content']}\n"
    return texto

while True:
    pregunta=input("pregunta: ")
    if (pregunta=="0"):
        break    
    historial=Contruir_Memoria()
    print("memoria: ",memoria)
    respuesta=pipeline.invoke({"pregunta":pregunta,"memoria":historial})
    print("Asistente: ",respuesta)

    #guardar memoria
    memoria.append({"role":"user","content":pregunta})
    memoria.append({"role":"asistent","content":respuesta})
    