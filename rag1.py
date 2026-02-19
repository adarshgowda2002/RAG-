import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from pymongo import MongoClient

client = OpenAI()

mongo = MongoClient(os.getenv("MONGO_URI"))
collection = mongo["rag_db"]["docs"]

CHAT="gpt-4o-mini"
EMBED="text-embedding-3-large"


def embed(text):
    return client.embeddings.create(
        model=EMBED,
        input=text
    ).data[0].embedding


def retrieve(query):

    qv=embed(query)

    pipeline=[{
        "$vectorSearch":{
            "index":"vector_index",
            "path":"embedding",
            "queryVector":qv,
            "limit":5,
            "numCandidates":200
        }
    },{
        "$project":{"text":1,"_id":0}
    }]

    docs=list(collection.aggregate(pipeline))

    return [d["text"] for d in docs]


def ask(query):

    ctx=retrieve(query)

    prompt=f"""
Answer ONLY using this context:

{ctx}

Question: {query}
"""

    res=client.chat.completions.create(
        model=CHAT,
        messages=[{"role":"user","content":prompt}]
    )

    return ctx,res.choices[0].message.content
