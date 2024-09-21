import os
import json
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient, errors
import numpy as np
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Load MongoDB password
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
if not MONGODB_PASSWORD:
    raise ValueError("MONGODB_PASSWORD environment variable is not set")

# Load MiniLM model (all-MiniLM-L6-v2)
try:
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
except Exception as e:
    raise RuntimeError(f"Error loading MiniLM model: {e}")

# Connect to MongoDB Atlas
try:
    client = MongoClient(
        f"mongodb+srv://testing_user:{MONGODB_PASSWORD}@userdata.r3vkc.mongodb.net/?retryWrites=true&w=majority&appName=UserData"
    )
    db = client["matchtube"]  # Replace with your actual database name
    collection = db["youtube"]  # Replace with your collection name
except errors.ConnectionError as e:
    raise RuntimeError(f"Error connecting to MongoDB Atlas: {e}")
except errors.ConfigurationError as e:
    raise RuntimeError(f"Configuration error with MongoDB Atlas: {e}")


# Upload a user's data
def upload_user_data(user_id: str, video_data: list[dict]) -> None:
    """
    Takes a user's video data and generates embeddings to upload to MongoDB.
    :param user_id: The user's unique identifier (username, etc.).
    :param video_data: A list of dictionaries containing video details. Each video should have keys 'title', 'channel_title', 'description', and 'tags'.
    """
    # Extract and concatenate video details (title, channel_title, description, and tags)
    video_texts = [
        f"{video['title']} {video['channel_title']} {video['description']} {' '.join(video['tags'])}"
        for video in video_data
    ]

    # Generate embeddings for each video
    video_embeddings = model.encode(video_texts)

    # Optionally, create an aggregated user embedding (e.g., average of all video embeddings)
    user_embedding = np.mean(video_embeddings, axis=0)

    # Store the overall user embedding
    user_data = {
        "user_id": user_id,
        "user_embedding": user_embedding.tolist(),  # Convert to list for MongoDB
    }

    # Upload the embeddings to MongoDB
    collection.update_one({"user_id": user_id}, {"$set": user_data}, upsert=True)


# Function to get the embedding of a specific user
def _get_user_embedding(user_id):
    user_data = collection.find_one({"user_id": user_id})
    return user_data["user_embedding"] if user_data else None


# Function to find closest user using Atlas Search
def _find_closest_user(target_user_id, target_embedding):
    # Define the number of candidates and results you want
    num_candidates = 100  # Adjust as needed
    limit = 3  # Number of closest users to return

    # Perform a vector search using Atlas Search
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",  # Replace with your actual index name
                "path": "user_embedding",  # Ensure this matches the field in your documents
                "queryVector": target_embedding,  # The target user's embedding
                "numCandidates": num_candidates,
                "limit": limit,
            }
        },
    ]

    closest_user = list(collection.aggregate(pipeline))

    if closest_user:
        if closest_user[0]["user_id"] == target_user_id:
            closest_user.pop(0)
        # print(f"The closest user to {target_user_id} is {closest_user[0]['user_id']}.")
        return closest_user[0]["user_id"]
    else:
        # print("No closest user found.")
        return None


def find_closest_user(user_id: str) -> str | None:
    """
    Find the closest user to a target user based on embeddings.
    :param target_user_id: The user ID of the target user.
    """
    # Example usage: Query the closest user based on a specific user's embedding
    target_embedding = _get_user_embedding(user_id)

    # print(type(target_embedding), target_embedding)

    if target_embedding:
        return _find_closest_user(user_id, target_embedding)
    else:
        return None
