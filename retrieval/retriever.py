import numpy as np
from sentence_transformers import SentenceTransformer
from vectorstore.vectordb import load_index

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, k=3):

    index = load_index()

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    return indices