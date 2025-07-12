from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

# Connect to MongoDB using the environment variables
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Access collections
datasets_collection = db.get_collection("datasets")
quality_logs_collection = db.get_collection("quality_logs")
