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
   ![Screenshot 2025-06-13 141304](https://github.com/user-attachments/assets/a427442e-cabf-427a-8bb8-1355fa708af0)

   ###
2) Options like uploading a file or pasting your code can be done
   ###
   ![Screenshot 2025-06-13 141427](https://github.com/user-attachments/assets/b882fac3-c203-4d3f-aa19-5269e3729d65)

  ###
3) After uploading or pasting the code and pressing Enter, the code will be processed. After which, one can ask further questions about the code
   ###
   ![Screenshot 2025-06-13 141540](https://github.com/user-attachments/assets/4741fc85-2360-474a-8cb9-51506b8935d6)

  ###
4) The response will be displayed on the screen
   ###
   ![Screenshot 2025-06-13 141639](https://github.com/user-attachments/assets/3475c399-98fd-43d9-beed-6224874d7609)



