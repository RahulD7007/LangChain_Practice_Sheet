from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel 


model = ChatOllama(model = 'gemma3:4b')

template1 = PromptTemplate(
    template = 'Generate a single but short tweet for {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Generate a single but short linkedIn post for {topic} (dont give multiple options to choose from)',
    input_variables = ['topic']
)

parser = StrOutputParser()

parallel = RunnableParallel({
    'tweet' : RunnableSequence(template1 ,model ,parser),
    'post' : RunnableSequence(template2 ,model ,parser)
})

res = parallel.invoke({'topic' : 'new job as AI engineer'})


print(f'Tweet -> {res['tweet']}')
print('*' * 125)
print(f'Post -> {res['post']}')


