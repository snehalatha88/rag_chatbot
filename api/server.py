from fastapi import FastAPI
from pipeline.rag_pipeline import ask_question, build_vector_store

app = FastAPI()

chunks = build_vector_store()

@app.get("/")
def home():
    return {"message": "RAG API running"}

@app.post("/chat")
def chat(question: str):

    answer = ask_question(question, chunks)

    return {"answer": answer}