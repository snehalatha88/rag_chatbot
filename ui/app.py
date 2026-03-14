import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline.rag_pipeline import build_vector_store, ask_question

st.title("RAG Chatbot")

if "chunks" not in st.session_state:
    st.session_state.chunks = build_vector_store()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask a question")

if question:

    st.session_state.messages.append({"role":"user","content":question})

    with st.chat_message("user"):
        st.write(question)

    answer = ask_question(question, st.session_state.chunks)

    st.session_state.messages.append({"role":"assistant","content":answer})

    with st.chat_message("assistant"):
        st.write(answer)