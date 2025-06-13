import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

st.set_page_config(page_title="Ask Your Python Code", layout="wide",page_icon="download.jpeg")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Functions
def split_python_code(code: str):
    import re
    pattern = re.compile(r"(def .+?:|class .+?:)")
    lines = code.splitlines()
    chunks = []
    buffer = []

    for line in lines:
        if pattern.match(line.strip()) and buffer:
            chunks.append("\n".join(buffer))
            buffer = [line]
        else:
            buffer.append(line)
    if buffer:
        chunks.append("\n".join(buffer))
    return chunks

def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

def search_chunks(query, chunks, index):
    query_vec = model.encode([query])
    _, I = index.search(query_vec, k=3)
    return [chunks[i] for i in I[0]]

def ask_llama(context, question):
    prompt = f"""You are a helpful AI assistant that answers questions about Python code.

Code Context:
{context}

Question:
{question}

Answer:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]

# UI
st.title("🐍 Ask Your Python Code (LLaMA RAG)")
code =None
code_input_method = st.radio("Choose Input Method:", ["Upload .py File", "Paste Code"])

if code_input_method == "Upload .py File":
    uploaded_file = st.file_uploader("Upload Python File", type="py")
    if uploaded_file:
        code = uploaded_file.read().decode()
else:
    code = st.text_area("Paste your Python code here", height=300)

if code:
    chunks = split_python_code(code)
    index, _ = embed_chunks(chunks)
    st.success("Code processed. Ask your question!")

    question = st.text_input("Ask something about the code:")
    if question:
        relevant_chunks = search_chunks(question, chunks, index)
        context = "\n\n".join(relevant_chunks)
        answer = ask_llama(context, question)
        st.markdown("### 🤖 Answer")
        st.write(answer)