import ollama, chromadb
from anthropic_api_usage import send_query_to_anthropic

def get_cv_feedback(cv_text):

    chroma = chromadb.HttpClient(host="localhost", port=8000)
    collection = chroma.get_or_create_collection("RAG-Collection")

    query = " ".join(cv_text)
    queryembed = ollama.embeddings(model="nomic-embed-text", prompt=query)['embedding']


    relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)["documents"][0]
    docs = "\n\n".join(relevantdocs)

    modelquery = f"{cv_text} - Answer that question using the following text as a resource: {docs}"

    return send_query_to_anthropic(modelquery)