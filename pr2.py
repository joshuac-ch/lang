from langchain_openai import ChatOpenAI
#from langchain_core.prompts import ChatPromptTemplate
#from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain

#from langchain.agents import Tool, AgentExecutor, create_openai_tools_agent
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate

#from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

api_key_grok = os.getenv("GROK_API_KEY")


# Crear el modelo
model = ChatOpenAI( 
    model="llama-3.1-8b-instant",
    api_key=api_key_grok,
    base_url="https://api.groq.com/openai/v1")

#plantilla promp
template=ChatPromptTemplate.from_messages([
   ("system","eres un asistente inteligente "),
   ("user","{pregunta}")
])

#parser
parser= StrOutputParser()

# Pipeline o chain estilo nuevo
chain=RunnableSequence(template,model,parser)

# Enviar al modelo ejecutar
respuesta = chain.invoke({"pregunta":"django"})

print("\n=== RESPUESTA ===")
print(respuesta)