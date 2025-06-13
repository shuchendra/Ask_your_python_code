# Ask_Your_Python_Code

## Features
Built a Python code understanding tool using Retrieval-Augmented Generation (RAG) powered by LLaMA-3, enabling users to ask natural language questions about uploaded or pasted .py files.

* Implemented semantic code chunking and retrieval with SentenceTransformers (MiniLM) and FAISS vector search, supporting context-aware question answering.

* Integrated local LLaMA 3 model inference via Ollama API to provide fast, offline code explanations without relying on cloud APIs.

* Designed auto-detection and visualization of common data structures (stack, queue, linked list, binary tree) using regex + AST parsing, with dynamic rendering via Graphviz, NetworkX, and Matplotlib.

* Developed an interactive Streamlit UI supporting dual input modes (file upload, raw code) and dual functionality (QA + visualization), enhancing accessibility for developers and students.

* Optimized the system to process and embed Python code functions and classes for efficient retrieval and contextual reasoning.

* Enhanced explainability and debugging by combining code analysis, chunk-based vector embedding, and open-source LLM-driven generation.<br>

## Requirements 
Refer to requirements.txt to know the versions required to run the application<br>
### `pip install -r requirements.txt` <br>
is the command to install Python packages

## Technologies Used
Python, Streamlit, SentenceTransformers, FAISS, Graphviz, NetworkX, Matplotlib, Ollama, LLaMA 3, RAG

## Demo
1) To run the code, go to the terminal and enter command -
   ### `streamlit run app.py`
   After running, the below screen is displayed
   ![Screenshot 2025-06-13 132719](https://github.com/user-attachments/assets/36d0e043-7a5f-453a-b286-10bbecbee905)
   ###
2) Options like uploading a file or pasting your code can be done
   ###
   ![Screenshot 2025-06-13 132914](https://github.com/user-attachments/assets/b3b408d4-9633-4c35-b435-7e2786254653)
  ###
3) After uploading or pasting the code and pressing Enter, the code will be processed. After which one can ask further questions about the code
   ###
  ![Screenshot 2025-06-13 132944](https://github.com/user-attachments/assets/6dbb6a1e-f715-407c-b370-9f7dec101070)
  ###
4) Response will be displayed on the screen
   ###
   ![Screenshot 2025-06-13 133056](https://github.com/user-attachments/assets/f8acec41-11af-4b8f-91f2-65602c683a1e)


