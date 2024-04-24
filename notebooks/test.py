import json
import textwrap

# Utils
import time
import uuid
from typing import List
import numpy as np
# LangChain
import langchain
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline
# Import custom Matching Engine packages

# Import custom Matching Engine packages

import faiss
from faiss import IndexFlatL2
import numpy as np
import spacy
from langchain_community.embeddings import HuggingFaceEmbeddings
import json
import pdfplumber
from langchain_community.vectorstores import FAISS
import os
#from google.colab import files
import zipfile
from langchain.document_loaders import BigQueryLoader #Class for storing a piece of text and associated metadata.
from langchain_community.embeddings import GPT4AllEmbeddings
#from google.colab import drive
#drive.mount('/content/drive')
new_db = FAISS.load_local("/Users/sahuneha/Desktop/IISC/capstone-project-final/DOCQA/Embeddings/faiss_index_all-mpnet-base-v2", GPT4AllEmbeddings(),allow_dangerous_deserialization=True)
query = 'prolong alcohol intake impact human health?'
print(new_db.similarity_search(query))
# try:
#     docs = new_db.similarity_search(query)
# except Exception as e:
#     print(e,'\n')
# # Formatting docs
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# ## converting it into list of string to generate summary
# docs1=format_docs(docs)
# model_name="gpt2"
# chat_pipeline=pipeline("text-generation",model=model_name)

# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# from langchain.prompts import PromptTemplate

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)