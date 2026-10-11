from langchain_core.prompts import PromptTemplate, load_prompt

template = PromptTemplate(
    input_variables = ['topic', 'question'],
    template = '''I am learning about {topic} and I have a question - {question}, now give me answer in simple 2-3 lines.'''
)

template.save('template.json')

# -------------- Usage -->

loaded_temp = load_prompt('template.json')

topic, question = 'Biology', 'What is photosynthesis'

from langchain_ollama import ChatOllama
llm = ChatOllama(model = 'gemma3:4b')

chain = loaded_temp | llm 
result = chain.invoke({'topic' : topic, 'question' : question}) 
print(result.content)