# ---->>> Embedding MODEL *****************************************************************

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model = 'nomic-embed-text')  # ollama pull nomic-embed-text

line1 = 'This is 1st'
single_embed = embeddings.embed_query(line1)
# print(single_embed)

lines = [ 
    'This is 2nd',
    'This is 3rd'
]

multi_embed = embeddings.embed_documents(lines)
# print(multi_embed)


# ------------------------------- COSINE SIMILARITY --------------------------------------

from sklearn.metrics.pairwise import cosine_similarity

documents = [
    'Mahatma Gandhi was an Indian lawyer, leader, and activist',
    'Max Planck was a German theoretical physicist considered the founder of quantum theory',
    'Jason Voorhees is a fictional serial killer from the Friday the 13th horror film franchise'
]

query = 'Who is Jason Voorhees'

document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], document_embeddings)[0]
# idx, score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

import numpy as np
idx = np.argmax(scores)
score = scores[idx]

print(f'Score : {score:.4f}')
print(f'Query : {query}')
print(documents[idx])
