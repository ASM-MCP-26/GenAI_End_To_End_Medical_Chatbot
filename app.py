# Now lets create end point that means main application 
# Using flask 

from flask import Flask, render_template, jsonify,request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import * 
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os
from langchain_openai import OpenAI

app = Flask(__name__)

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Set environment variables properly
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = download_hugging_face_embeddings()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY )

 # index name 
index_name = "medical-chatbot"

# Now load Existing index
from langchain_pinecone import PineconeVectorStore
docsearch = PineconeVectorStore.from_existing_index(
                                                        index_name= index_name,
                                                        embedding=embeddings
                                                     )

# print the docs search 
docsearch

# Now you can also perform the retrieve operation here that you can perform the similarity search 
retriever = docsearch.as_retriever(search_type = 'similarity', search_kwargs = {"k" : 3})

llm = OpenAI(temperature= 0.4, max_tokens= 500)


prompt = ChatPromptTemplate.from_messages(
                                            [
                                                ("system", system_prompt),
                                                ("human","{input}")
                                            ]
                                         ) 

# Now create the chain 
question_answer_chain = create_stuff_documents_chain(llm, prompt)
# 
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


# Now create the two route
# First route would be my default route that means user will get the interface my application chat.

@app.route("/")
def index():
    return render_template("chat.html")

# Now 2nd route I'll doing for the chat operation that means user is giving any query to the chatbot so that messages actually will be accepting and this messages I will give to my llm   

@app.route("/get", methods = ['GET','POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response :", response['answer'])
    return str(response['answer'])


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 7152, debug= True )