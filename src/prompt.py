## prompt.py

# Now import some necessary library
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate

system_prompt = (
                    "You are an assistant for question-answering tasks."
                    "Use the following pieces of retrieved context to answer the question."
                    "If you don't know the answer, say that you don't know."
                    "USe three sentences maximum and keep the answer concise."
                    "\n\n"
                    "{context}"
                )