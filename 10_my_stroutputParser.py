# Returns Output format in String 

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'gemma3:4b', temperature = 0.2)

parser = StrOutputParser()

template1 = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write a detailed report on {topic}'
)

template2 = PromptTemplate(
    input_variables = ['text'],
    template = 'Generate 5 line summary for : {text}'
)

chain = template1 | model | parser | template2 | model | parser

res = chain.invoke({'topic' : 'Black holes'})
print(res)