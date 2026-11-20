from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import chromadb


load_dotenv()

chroma_client = chromadb.Client()


class Embeddings:
    def __init__(self, collection_name: str):
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large"
        )
        self.collection = chroma_client.get_or_create_collection(
            name=collection_name)

    def add_documents(self, documents: list):
        """
        Add documents to the collection.
        """
        self.collection.add(
            ids=[str(i) for i in range(len(documents))],
            documents=documents,
            embeddings=self.embeddings.embed_documents(documents)
        )
        return f"Added {len(documents)} documents to the collection."

    def query(self, query: str, n_results: int = 5):
        """
        Query the collection for similar documents.
        """
        query_embedding = self.embeddings.embed_query(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results
