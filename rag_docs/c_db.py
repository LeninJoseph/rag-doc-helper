import chromadb

# Connect to your persistent ChromaDB folder (or use chromadb.Client() if in-memory)
client = chromadb.PersistentClient(path="./chroma_db")

# Load your collection
collection = client.get_collection(name="interview_docs")

# 1. Check total number of stored chunks
print(f"Total items: {collection.count()}")

# 2. Quick preview of the first 10 items
preview = collection.peek()
print(preview["ids"])
print(preview["metadatas"])

# 3. Fetch documents and metadata (with an optional limit)
data = collection.get(
    limit=5,
    include=["documents", "metadatas"]
)

for doc_id, text, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"ID: {doc_id}")
    print(f"Metadata: {meta}")
    print(f"Content: {text[:150]}...\n" + "-"*40)
