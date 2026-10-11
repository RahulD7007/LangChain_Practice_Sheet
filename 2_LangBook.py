# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LANGCHAIN >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 



# ---->>> CHAT MODEL **********************************************************************


from langchain_ollama import ChatOllama

llm = ChatOllama(model = 'gemma3:4b', temperature = 0.9, max_completion_tokens=12)
response = llm.invoke('What is LLM?')
print(response.content)



# ---->>> PromptTemplate ******************************************************************

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables = ['topic', 'n'],
    template = 'Explain {topic} in {n} lines'
)
# myPrompt = prompt_template.invoke({'topic':'Black holes', 'n' : 3})

myPrompt = prompt_template.format(topic = 'Black holes', n = 3)
# print(myPrompt)
# print(llm.invoke(myPrompt).content)