# RunnablePassThrough is depricated, use RunnableLambda instead

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnableLambda
)

model = ChatOllama(model = 'gemma3:4b')

template1 = PromptTemplate(
    template = 'Generate a small joke on {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Explain this joke - {joke}',
    input_variables = ['joke']
)

parser = StrOutputParser()

jokeGenerator = RunnableSequence(template1, model, parser)

meaningGen = RunnableParallel({
    'joke' : RunnableLambda(lambda x: x),
    'meaning' : RunnableSequence(template2, model, parser)
})

chain = RunnableSequence(jokeGenerator, meaningGen)

print(chain.invoke({'topic' : 'Cricket'}))
