# Introduction 
Retrieval Augmented Generation (RAG) is a pattern that works with pretrained Large Language Models (LLM) and your own data to generate responses.

It combines the powers of pretrained dense retrieval and sequence-to-sequence models. RAG models retrieve documents, pass them to a seq2seq model, then marginalize to generate outputs.

In this project Dataset which is used is Pubmed and different pdf Journals downloaded from web.Reference of Dataset is present in Data folder. There is one out.csv which contains text extracted from PDF. This data was extracted and stored in Bigquery because of the size of the data.

# Getting Started
Follow below steps for local setup
Clone the repository from https://github.com/Nehakumari-01988/DOCQA.git


Data source:
    pdf: Pdf of Medical Reserach Journals
    pdf_extracted.csv: Text output extracted from BQ once all PDF was processsed through Data cleansing.

Notebooks:
    1. pubmed_capstone_project_Dataset.ipynb:script to download dataset from pubmed and extract textfrom pdf
    2.Pubmed_capstone_Project_embedding_Indexing_Faissall_mpnet_base_v2:Build Rag using opensource faiss db and gpt4all llm
    3.Build RAG using cloud storage/geckoembedding/vertex DB
    4.Pubmed_capstone_Project_embedding_Indexing_Faiss_Faissall_mpnet_base_v2frontend.ipynb:Frontend code using Gradio


Reports:Next-Gen Answers_ Leveraging RAG and LLMs for Enhanced Medical Q&A on PubMed.pdf

requirements.txt # Python dependencies
 