from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json

model = ChatOllama(model = 'gemma3:4b')

chatHistory = [
    SystemMessage(content = 'You are role playing of a girlfriend'),
]

while True:
    inp = input('You :')
    if inp == 'bye':
        break
    
    chatHistory.append(HumanMessage(content = inp))
    res = model.invoke(chatHistory)

    chatHistory.append(AIMessage(content = res.content))
    print('AI :', res.content)

print(chatHistory)

with open('./chatbotHistory.txt', 'w', encoding='utf-8') as f:
    for msg in chatHistory:
        msg_type = msg.__class__.__name__  # HumanMessage / AIMessage / SystemMessage
        f.write(f'{msg_type}(content="{msg.content}")\n')