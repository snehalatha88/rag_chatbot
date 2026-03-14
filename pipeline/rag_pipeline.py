from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from ingestion.embedder import create_embeddings
from vectorstore.vectordb import create_index
from retrieval.retriever import retrieve
from llm.llm_client import generate_answer


def build_vector_store():

    docs = load_documents()
    print("Loaded docs:", docs)

    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))

    print("Chunks:", chunks)

    embeddings = create_embeddings(chunks)
    print("Embeddings shape:", embeddings.shape)

    create_index(embeddings)

    return chunks


def ask_question(question, chunks):

    indices = retrieve(question)

    context = ""

    for i in indices[0]:
        context += chunks[i] + "\n"

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    return answer