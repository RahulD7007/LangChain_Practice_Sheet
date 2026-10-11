from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableBranch

model = ChatOllama(model = 'gemma3:4b')

template = PromptTemplate(
    template = 'Generate a report for {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Give a short summary for this report - {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

report_gen_chain = template | model | parser    # -> LCEL (LangChain Expression Language)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, template2 | model | parser),
    RunnableLambda(lambda x: x)
)

chain = report_gen_chain | branch_chain


print(chain.invoke({'topic' : 'Quantum Physics'}))