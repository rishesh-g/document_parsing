import os
import config

os.environ["LANGSMITH_TRACING"] = config.LANGSMITH_TRACING
os.environ["LANGSMITH_API_KEY"] = config.LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = config.LANGSMITH_PROJECT
# os.environ["LANGCHAIN_ENDPOINT"] = config.LANGSMITH_ENDPOINT


from utils import  prompt_func
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(model=config.MODEL, temperature=config.TEMPERATURE, format = 'json')
chain = prompt_func | llm | StrOutputParser()

def get_response(**kwargs):

    response = chain.invoke(
        kwargs
    )

    return response