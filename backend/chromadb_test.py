import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("HUGGINGFACE_API_KEY")

huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key=api_key,
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# Initialize ChromaDB with the custom embedding function
chroma_client = chromadb.Client()
# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(
    name="my_collection",
    embedding_function=huggingface_ef,  # Use Hugging Face embeddings
)

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
    ],
    ids=["id1", "id2"],
)

results = collection.query(
    query_texts=["hawaii"],  # Chroma will embed this for you
    n_results=2,  # how many results to return
)

print(json.dumps(results, indent=2))
