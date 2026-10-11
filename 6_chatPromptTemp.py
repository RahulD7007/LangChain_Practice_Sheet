from langchain_core.prompts import ChatPromptTemplate

chat_temp = ChatPromptTemplate([
    ('system', 'You are a professional {domain} expert'),
    ('human', 'Explain what is {topic}')
])

prompt = chat_temp.invoke({'domain':'AI', 'topic':'LLM'})
# print(prompt)

# -------------------------------------------------------------------------------------------------

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_temp = ChatPromptTemplate([
    ('system', 'you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human', '{query}')
])

chat_history = []

with open('history.txt') as f:
    chat_history.extend(f.readlines())

prompt = chat_temp.invoke({'chat_history':chat_history, 'query':'where is my refund'})

print(prompt)

# from langchain_ollama import ChatOllama
# model = ChatOllama(model= 'gemma3:4b')

# print(model.invoke(prompt).content)