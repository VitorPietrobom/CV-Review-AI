import ollama, chromadb, time
from utilities import readtext
from mattsollamatools import chunk_text_by_sentences

collectionname="RAG-Collection"

chroma = chromadb.HttpClient(host="localhost", port=8000)
print(chroma.list_collections())
if any(collection.name == collectionname for collection in chroma.list_collections()):
  print('deleting collection')
  chroma.delete_collection(collectionname)
collection = chroma.get_or_create_collection(name=collectionname, metadata={"hnsw:space": "cosine"})

starttime = time.time()
with open('sourcedocs.txt') as f:
  lines = f.readlines()
  for filename in lines:
    text = readtext(filename)
    chunks = chunk_text_by_sentences(source_text=text, sentences_per_chunk=7, overlap=0 )
    print(f"with {len(chunks)} chunks")
    for index, chunk in enumerate(chunks):
        try:
            embed = ollama.embeddings(model="nomic-embed-text", prompt=chunk)['embedding']
            print(".", end="", flush=True)
            collection.add([filename+str(index)], [embed], documents=[chunk], metadatas={"source": filename})
        except Exception as e:
            print(e)
    
print("--- %s seconds ---" % (time.time() - starttime))