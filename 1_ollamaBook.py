# ollama run llama2
# ollama --help

# ollama list
# ollama pull tinyllama:latest
# ollama list

# pip install ollama
# python

# import ollama
# response = ollama.chat(model='tinyllama:latest', messages=[{'role': 'user', 'content': 'Hello!'}])
# response
# response['message']
# response['message']['content']

# ollama rm <mod_name>

# ------------------------------------- OLLAMA ---------------------------------------------

import ollama
# ollama pull gemma3:4b

response = ollama.chat(model = 'gemma3:4b', messages = [{
    'role' : 'user',
    'content' : 'What is LLM?'
}])

print(response.message.content)