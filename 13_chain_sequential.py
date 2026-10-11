from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---->>> SEQUENTIAL CHAIN *****************************************************************

model = ChatOllama(model = 'gemma3:4b')

template1 = PromptTemplate(
    template = 'Give detailed report about {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Give 5 important lines from :\n{resp}',
    input_variables = ['resp']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
res = chain.invoke({'topic' : 'Time Travel'})
print(res)

# chain.get_graph().print_ascii()    # Requires pip install grandalf

