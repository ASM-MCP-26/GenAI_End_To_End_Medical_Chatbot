from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

# data extract by a function from a pdf file 
extracted_data = load_pdf_file(data = 'Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings() 

# Pinecone api key and environment
pc = Pinecone(api_key=PINECONE_API_KEY )
 # index name 
index_name = "medical-bot"

pc.create_index(
                name = index_name,
                dimension= 384,
                metric= "cosine",
                spec=ServerlessSpec(
                                    cloud= 'aws',
                                    region= 'us-east-1'
                                   )
               )

# To store the vector embeddings embed each chunk and upsert the embeddings in your pinecone index.
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
                                                documents= text_chunks,
                                                index_name = index_name,
                                                embedding= embeddings
                                              )