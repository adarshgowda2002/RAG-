from fastapi import FastAPI
from rag_engine import ask
from subfolder.rag_engine import ask

app=FastAPI()

@app.get("/ask")
def query(q:str):

    ctx,ans=ask(q)

    return {
        "answer":ans,
        "context":ctx
    }
