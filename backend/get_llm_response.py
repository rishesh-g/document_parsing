import config
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