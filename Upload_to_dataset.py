# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:36:06 2024

@author: 10364

pip install tiktoken==0.6.0
pip install openai==0.28.1
pip install pinecone-client==2.2.4
pip install langchain==0.0.292
pip install unstructured==0.10.30

https://app.pinecone.io/
"""

#load the documents from content/data dir
directory = 'D:/Project/Python/paper/paper4/Sample_data'
import os
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


from langchain.document_loaders import DirectoryLoader
# load_docs functions to load documents using langchain function
def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents

documents = load_docs(directory)
print(len(documents))


from langchain.text_splitter import RecursiveCharacterTextSplitter
# split the docs using recursive text splitter
def split_docs(documents, chunk_size = 200, chunk_overlap = 20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

# split the docs
docs = split_docs(documents)
print(len(docs))

from langchain.embeddings.openai import OpenAIEmbeddings
# embedding example on random word
embeddings = OpenAIEmbeddings()

import pinecone
# initiate pinecondb
pinecone.init(api_key="3539a858-2aa1-445b-998e-c01612cc1c36", environment="gcp-starter")

# define index name
index_name = "czh"

from langchain.vectorstores import Pinecone
# store the data and embeddings into pinecone index
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)