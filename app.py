import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

st.set_page_config(page_title="Ask Your Python Code", layout="wide",page_icon="download.jpeg")

# load embedding model "MiniLM-L6-V2
model = SentenceTransformer("all-MiniLM-L6-v2")

# function to split python code to chunks based on Classes and functions
def split_python_code(code: str):
    import re
    pattern = re.compile(r"(def .+?:|class .+?:)")
    lines = code.splitlines() # to split the code into single lines
    chunks = [] #list to store final chunks
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

#function to generate embeddings for the chunks and index them using FAISS
def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

#function that will search top relevent code chunks for the query
def search_chunks(query, chunks, index):
    query_vec = model.encode([query])
    _, I = index.search(query_vec, k=3)
    return [chunks[i] for i in I[0]]

#function to send the selected context and questions to LLAMA for answers 
def ask_llama(context, question):
    prompt = f"""You are a helpful AI assistant that answers questions about Python code.

Code Context:
{context}

Question:
{question}

Answer:"""

    #sending prompt to local LLAMA api
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]

#User Interface - UI
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
        answer = ask_llama(context, question) #getting answer from LLAMA
        st.markdown("### 🤖 Answer") Displaying the answer
        st.write(answer)
