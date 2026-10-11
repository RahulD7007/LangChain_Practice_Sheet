from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda

model = ChatOllama(model = 'gemma3:4b')

template = PromptTemplate(
    template = 'Generate a simple joke about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

jokeGenerator = RunnableSequence(template, model, parser)

def word_count(word):
    return len(word.split())

lenCounter = RunnableParallel({
    'joke' : RunnableLambda(lambda x: x),
    'len' : RunnableLambda(word_count)
    # 'len' : RunnableLambda(lambda x: len(x.split()))
})

chain = RunnableSequence(jokeGenerator, lenCounter)

res = chain.invoke({'topic':'unemployment'})

print(f'Joke : {res['joke']}\nWord Count : {res['len']}')