import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from pymongo import MongoClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter

client = OpenAI()
mongo = MongoClient(os.getenv("MONGO_URI"))
collection = mongo["rag_db"]["docs"]

EMBED="text-embedding-3-large"


def embed(text):
    return client.embeddings.create(
        model=EMBED,
        input=text
    ).data[0].embedding


loader = PyPDFLoader("pdfs/1.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

records=[]

for c in chunks:
    records.append({
        "text":c.page_content,
        "embedding":embed(c.page_content)
    })

collection.insert_many(records)

# CREATE VECTOR INDEX
collection.create_search_index({
    "name":"vector_index",
    "definition":{
        "fields":[{
            "type":"vector",
            "path":"embedding",
            "numDimensions":3072,
            "similarity":"cosine"
        }]
    }
})

print("PDF INGESTED")
