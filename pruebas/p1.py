from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
apykey=os.getenv('GROK_API_KEY')
modelo=ChatOpenAI(model="llama-3.1-8b-instant",base_url="https://api.groq.com/openai/v1",api_key=apykey)

template=ChatPromptTemplate.from_messages([
    ("system","eres un asistente con una caracteristica tsundere"),
    ("user","{pregunta}")
])
salida=StrOutputParser()
pipeline=RunnableSequence(template,modelo,salida)


respuesta=pipeline.invoke({"pregunta":"resumen de la toma de la bastilla"})
print(respuesta)