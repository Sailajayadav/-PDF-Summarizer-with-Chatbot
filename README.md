#PDF Summarizer with Chatbot
This project is a *PDF Summarizer* and *Chatbot* web application built using *Streamlit* and *OpenAI's API*. Users can upload a PDF file, extract text from it, and interact with a chatbot to ask questions about the content
## Features
- *Upload PDFs*: Allows users to upload PDF documents.
- *Text Extraction*: Extracts and processes text from the uploaded PDF.
- *Chunking*: Splits the text into manageable chunks for processing.
- *Embeddings*: Uses OpenAI embeddings to vectorize the text for semantic search.
- *Interactive Chat*: Users can ask questions related to the uploaded PDF content, and the chatbot provides answers.
- *Streamlit Interface*: A clean and user-friendly web interface.
### *Python Version*
- Python 3.7 or later
### *Libraries*
Install the following dependencies using pip:
```bash
pip install streamlit PyPDF2 langchain openai faiss-cpu langchain-community
