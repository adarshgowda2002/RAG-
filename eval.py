from ragas import evaluate
from datasets import Dataset
from rag_engine import ask

questions=[
"What is the document about?",
"Explain main topic"
]

ground_truth=[
"Document describes the subject",
"Main topic explanation"
]

rows=[]

for q,g in zip(questions,ground_truth):

    ctx,ans=ask(q)

    rows.append({
        "question":q,
        "contexts":ctx,
        "answer":ans,
        "ground_truth":g
    })

dataset=Dataset.from_list(rows)

result=evaluate(dataset)

print(result)
