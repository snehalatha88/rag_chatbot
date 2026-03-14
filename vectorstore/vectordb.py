import faiss
import numpy as np

INDEX_PATH = "vectorstore/index.faiss"

def create_index(embeddings):

    embeddings = np.array(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    return index


def load_index():

    index = faiss.read_index(INDEX_PATH)

    return index