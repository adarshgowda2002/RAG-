import matplotlib.pyplot as plt

metrics={
"faithfulness":0.92,
"answer_relevancy":0.71,
"context_recall":0.96,
"context_precision":0.96,
"relevance_rate":0.94
}

plt.figure()
plt.bar(metrics.keys(),metrics.values())
plt.axhline(0.7,linestyle="--")
plt.xticks(rotation=40)
plt.title("RAG Evaluation Metrics")
plt.show()
