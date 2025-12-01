from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
import os
import sys
load_dotenv()
API_KEY_GROK=os.getenv("GROK_API_KEY")

#crear el modelo y que sea en tiempo real
model=ChatOpenAI(model="llama-3.1-8b-instant",api_key=API_KEY_GROK,base_url="https://api.groq.com/openai/v1",streaming=True)


#template
promp=ChatPromptTemplate.from_messages([
    ("system","Eres una asistente que tiene las caracteristicas de una chica tsundere como nino nakano"),
   
    ("user","{pregunta}")
])
#mejora de salida
parser=StrOutputParser()
#encadenamiento moderno
pipeline=RunnableSequence(promp,model,parser)


#ejecutar
texto="explicame que es Deep Learning de manera resumida"
for chunck in pipeline.stream({"pregunta":texto}):
    sys.stdout.write(chunck)
    sys.stdout.flush()

#respuesta=pipeline.invoke({"pregunta":texto})
#print(respuesta)