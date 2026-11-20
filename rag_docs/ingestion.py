from embeddings import Embeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from pathlib import Path
import asyncio

folder_path = Path(
    "/Users/leninjoseph/Documents/LENIN/Learning/RAG/doc_helper/data")


async def ingest():

    documents = []
    for file_path in folder_path.rglob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        documents.append((file_path.name, content))

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100)

    all_chunks = []

    for file_name, content in documents:
        markdown_chunks = markdown_splitter.split_text(content)
        for chunk in markdown_chunks:
            text_chunks = text_splitter.split_text(chunk.page_content)
            all_chunks.extend(text_chunks)

    if not all_chunks:
        raise RuntimeError(f"No chunks produced from {folder_path}")
    embeddings.add_documents(all_chunks)


def check_collection():
    results = embeddings.query("What is asyncio in python?", n_results=5)
    print(results)


if __name__ == "__main__":
    embeddings = Embeddings(collection_name="interview_docs")

    asyncio.run(ingest())
    check_collection()
