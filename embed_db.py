import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Create Hugging Face embedding function
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key=api_key,  # Your Hugging Face API Key
    model_name="sentence-transformers/all-MiniLM-L6-v2",  # Pre-trained model
)

# Create a collection in ChromaDB with the Hugging Face embedding function
collection = chroma_client.get_or_create_collection(
    name="people_collection",
    embedding_function=huggingface_ef,  # Set the embedding function
)

people_data = {}

# Iterate over folders in user_data directory, and parse video_data.json
for folder in os.listdir("user_data"):
    if os.path.isdir(os.path.join("user_data", folder)):
        with open(os.path.join("user_data", folder, "video_data.json"), "r") as f:
            video_data = json.load(f)
            people_data[folder] = video_data

# print(people_data)
# exit()

# Function to convert each person's video data into a single concatenated text
def aggregate_videos_text(videos):
    # Concatenate the title, description, and tags of each video
    aggregated_text = " ".join(
        [
            f"{video['title']} {video['channel_title']} {video['description']} {' '.join(video['tags'])}"
            for video in videos
        ]
    )
    return aggregated_text


# Add each person's aggregated video data as a document in the collection
for person, videos in people_data.items():
    person_text = aggregate_videos_text(videos)

    # Upsert into the collection (this will auto-embed using the Hugging Face model)
    collection.upsert(documents=[person_text], ids=[person])

# Query the collection for similar users based on embeddings
# Let's assume you want to find people similar to "sofia"
# query_text = aggregate_videos_text(people_data["sofia"])

# Query the collection (n_results=2 to find the closest matches)
# results = collection.query(query_texts=[query_text], n_results=2)

# Print the results
# print(results["ids"], results["distances"])

for person, videos in people_data.items():
    results = collection.query(query_texts=[aggregate_videos_text(videos)], n_results=5)
    comparisons = list(zip(results["ids"], results["distances"]))
    # print(person, results["ids"], results["distances"])
    print(person, comparisons)
