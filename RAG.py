import os 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter    
from openai import OpenAIClient
from pymongo import MongoClient, results
import time
from pymongo.operations import SearchIndexModel
os.environ["OpENAI_API_KEY"] = ""
client = MongoClient("")
collection =  client["rag_db"]["test"]



client = OpenAIClient()
model = "text-embedding-3-large"

def get_embedding(text,input="document"):
    response = client.embeddings.create(
        model=model,
        input=text,
    )
    return response.data[0].embedding


loader = PyPDFLoader("pdfs/1.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
document = text_splitter.split_documents(data)

doc_to_insert=[
    {
        "text":doc.page_content,
        "embedding":get_embedding(doc.page_content)

    }for doc in document
]

doc_to_insert

collection=client["rag_db"]["test"]
result = collection.insert_many(doc_to_insert)


index_name = "vector_index"
search_index_model = SearchIndexModel(
    definition={
        "type":"vector",
        "numDimensions":1024,
        "path":"embedding",
        "similarity": "cosine"
    },
    name=index_name,
    type="vectorsearch",
)
collection.create_index(search_index_model)

print("Polling to check if the index is ready. This may take up to a minute.")
predicate=None
if predicate is None:
   predicate = lambda index: index.get("queryable") is True

while True:
   indices = list(collection.list_search_indexes(index_name))
   if len(indices) and predicate(indices[0]):
      break
   time.sleep(5)
print(index_name + " is ready for querying.")

query_embedding = get_embedding("What is the main topic of the document?")

results = collection.aggregate([
   {
      "$vectorSearch": {
         "index": "vector_index",
         "path": "embedding",
         "queryVector": query_embedding,
         "numCandidates": 3072,
         "limit": 5
      }
   }
])
array_of_results =[]
for doc in results:
    array_of_results.append(doc)


array_of_results

# Define a function to run vector search queries
def get_query_results(query):
  """Gets results from a vector search query."""

  query_embedding = get_embedding(query, input_type="query")
  print(query_embedding)
  pipeline = [
      {
            "$vectorSearch": {
              "index": "vector_index",
              "queryVector": query_embedding,
              "path": "embedding",
              "numCandidates":3072,
              "limit": 5
            }
      }, {
            "$project": {
              "_id": 0,
              "text": 1
         }
      }
  ]

  results = collection.aggregate(pipeline)
  print(results)

  array_of_results = []
  for doc in results:
      array_of_results.append(doc)
  return array_of_results

get_query_results("What is the main topic of the document?")

query = "What are MongoDB's latest AI announcements?"
context_docs = get_query_results(query)
context_string = " ".join([doc["text"] for doc in context_docs])

# Construct prompt for the LLM using the retrieved documents as the context
prompt = f"""Use the following pieces of context to answer the question at the end.
    {context_string}
    Question: {query}
"""

openai_client = OpenAI()

# OpenAI model to use
model_name = "gpt-4o"

completion = openai_client.chat.completions.create(
model=model_name,
messages=[{"role": "user",
    "content": prompt
  }]
)
print(completion.choices[0].message.content)