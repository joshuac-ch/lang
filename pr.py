from langchain_openai import ChatOpenAI
#from langchain_core.prompts import ChatPromptTemplate
#from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain

#from langchain.agents import Tool, AgentExecutor, create_openai_tools_agent
import os
from dotenv import load_dotenv

load_dotenv()

api_key_grok = os.getenv("GROK_API_KEY")


# Crear el modelo
model = ChatOpenAI( 
    model="llama-3.1-8b-instant",
    api_key=api_key_grok,
    base_url="https://api.groq.com/openai/v1")
#plantilla

texto=input("ingrese su pregunta: ")
# Enviar al modelo
respuesta = model.invoke(texto)

print("\n=== RESPUESTA ===")
print(respuesta.content)