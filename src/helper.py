# helper.py
# from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

# extract the data from pdf files
def load_pdf_file (data):
    loader = DirectoryLoader(data,
                             glob= "*.pdf",
                             loader_cls= PyPDFLoader)
    document = loader.load()
    return document


# Now split the data into text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap =  20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


# Download the embeddings model from hugging face
from langchain.embeddings import HuggingFaceEmbeddings
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings