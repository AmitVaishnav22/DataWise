from utils.db import datasets_collection
from bson.objectid import ObjectId
from datetime import datetime
from bson.errors import InvalidId


def create_dataset(data):
    """
    Create a new dataset document in the MongoDB collection.
    Adds timestamps and marks the document as not deleted.
    """
    try:
        data.update({
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "is_deleted": False
        })
        result = datasets_collection.insert_one(data)
        new_data = datasets_collection.find_one({"_id": result.inserted_id})

        if new_data:
            new_data["_id"] = str(new_data["_id"])  
            return new_data

        return None
    except Exception as e:
        print(f"Error creating dataset: {e}")
        return None

def get_datasets(filters={}):
    """
    Retrieve a list of all non-deleted datasets.
    Accepts optional filters (e.g., by owner or tags).
    """
    try:
        filters["is_deleted"] = False
        return list(datasets_collection.find(filters))
    except Exception as e:
        print(f"Error retrieving datasets: {e}")
        return []


def get_dataset_by_id(dataset_id):
    """
    Retrieve a single dataset by its ID.
    Returns None if the dataset does not exist or is soft-deleted.
    """
    try:
        oid = ObjectId(dataset_id)
    except InvalidId:
        return None

    return datasets_collection.find_one({"_id": oid, "is_deleted": False})


def update_dataset(dataset_id, data):
    """
    Update an existing dataset by its ID.
    Automatically sets the updated_at timestamp.
    Returns the number of modified documents (0 or 1).
    """
    try:
        oid = ObjectId(dataset_id)
    except InvalidId:
        return 0

    data["updated_at"] = datetime.utcnow()
    result = datasets_collection.update_one(
        {"_id": oid, "is_deleted": False},
        {"$set": data}
    )
    return result.modified_count


def delete_dataset(dataset_id):
    """
    Soft delete a dataset by setting is_deleted to True.
    Returns the number of documents modified (should be 1 if successful).
    """
    try:
        oid = ObjectId(dataset_id)
    except InvalidId:
        return 0

    result = datasets_collection.update_one(
        {"_id": oid, "is_deleted": False},
        {"$set": {"is_deleted": True, "updated_at": datetime.utcnow()}}
    )
    return result
