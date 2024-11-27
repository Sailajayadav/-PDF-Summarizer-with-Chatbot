import streamlit as st
from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS 
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI  

OPENAI_API_KEY = "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"

st.header("My First Chatbot")

with st.sidebar: #for side bar in the website
    st.title("pdf summarizer")
    file= st.file_uploader("upload your pdf document", type = "pdf")

#to read & extract the data
if file is not None:
    pdf_reader= PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)

#break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size= 1000,
        chunk_overlap = 150,
        length_function = len
    )

    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    #generating embeddings 
    embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

    #Creating vector store 
    vector_store = FAISS.from_texts(chunks,embeddings)

    #user question 
    user_question = st.text_input("enter your question")

    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match)

        #define the llm
        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            temperature= 0,
            max_tokens=1000,
            model_name = "gpt-3.5-turbo"
        )
        
        #output results
        chain = load_qa_chain(llm, chain_type= "stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)

