import os
from pymongo import MongoClient
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Load MongoDB password from environment variable
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

# Connect to MongoDB Atlas
client = MongoClient(
    f"mongodb+srv://testing_user:{MONGODB_PASSWORD}@userdata.r3vkc.mongodb.net/?retryWrites=true&w=majority&appName=UserData"
)
db = client["matchtube"]
collection = db["youtube"]


# Function to list all users from the database
def list_all_users():
    # Retrieve all documents from the collection
    all_users = collection.find()

    # Check if there are users in the database
    if collection.count_documents({}) == 0:
        print("No users found in the database.")
        return

    # Print out all users and their details
    print(f"List of users: ({collection.count_documents({})})")
    for user in all_users:
        user_id = user.get(
            "user_id", "Unknown ID"
        )  # Default to 'Unknown ID' if user_id is not present
        print(f"User ID: {user_id}")


if __name__ == "__main__":
    # Call the function to list all users
    list_all_users()
