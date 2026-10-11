# Returns output format in Json but does not enforce schema

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(model = 'gemma3:4b')

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'Black Holes'})
# response = model.invoke(prompt)
# result = parser.parse(response.content)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

print(result) 
