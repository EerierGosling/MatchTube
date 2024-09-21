import os
import json
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import numpy as np
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Load MongoDB password
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

# Load MiniLM model (all-MiniLM-L6-v2)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connect to MongoDB Atlas
client = MongoClient(
    f"mongodb+srv://testing_user:{MONGODB_PASSWORD}@userdata.r3vkc.mongodb.net/?retryWrites=true&w=majority&appName=UserData"
)
db = client["matchtube"]  # Replace with your actual database name
collection = db["youtube"]  # Replace with your collection name

# User data folder
people_data = {}

# Step 1: Load user data from directories and parse video_data.json
for folder in os.listdir("user_data"):
    if os.path.isdir(os.path.join("user_data", folder)):
        with open(os.path.join("user_data", folder, "video_data.json"), "r") as f:
            video_data = json.load(f)
            people_data[folder] = video_data


# Step 2: Process each user's data
def process_user_data(user_id, video_data):
    # Extract and concatenate video details (title, channel_title, description, and tags)
    video_texts = [
        f"{video['title']} {video['channel_title']} {video['description']} {' '.join(video['tags'])}"
        for video in video_data
    ]

    # Generate embeddings for each video
    video_embeddings = model.encode(video_texts)

    # Optionally, create an aggregated user embedding (e.g., average of all video embeddings)
    user_embedding = np.mean(video_embeddings, axis=0)

    # Prepare the data for MongoDB
    # updated_videos = [
    #     {
    #         "title": video["title"],
    #         "channel_title": video["channel_title"],
    #         "description": video["description"],
    #         "tags": video["tags"],
    #         "embedding": video_embeddings[
    #             i
    #         ].tolist(),  # Convert to list for storage in MongoDB
    #     }
    #     for i, video in enumerate(video_data)
    # ]

    # Store the overall user embedding
    user_data = {
        "user_id": user_id,
        # "videos": updated_videos,
        "user_embedding": user_embedding.tolist(),  # Convert to list for MongoDB
    }

    # Step 3: Upload the user data to MongoDB
    collection.update_one({"user_id": user_id}, {"$set": user_data}, upsert=True)


# Step 4: Process all users and upload embeddings
if __name__ == "__main__":
    for user_id, video_data in people_data.items():
        process_user_data(user_id, video_data)

    print("Embeddings generated and uploaded successfully.")
