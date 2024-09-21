import os
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
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
db = client["matchtube"]
collection = db["youtube"]


# Function to get the embedding of a specific user
def get_user_embedding(user_id):
    user_data = collection.find_one({"user_id": user_id})
    return user_data["user_embedding"] if user_data else None


# Function to find closest user using Atlas Search
def find_closest_user_atlas(target_embedding):
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
        print(f"The closest user to {target_user_id} is {closest_user[0]['user_id']}.")
    else:
        print("No closest user found.")


if __name__ == "__main__":
    # Example usage: Query the closest user based on a specific user's embedding
    target_user_id = "yancheng"  # Replace with the actual user_id
    target_embedding = get_user_embedding(
        target_user_id
    )  # Use the previously defined function

    # print(type(target_embedding), target_embedding)

    if target_embedding:
        find_closest_user_atlas(target_embedding)
    else:
        print(f"User {target_user_id} not found in the database.")
