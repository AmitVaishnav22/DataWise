from utils.db import quality_logs_collection
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime


def add_quality_log(dataset_id, data):
    """
    Create a new quality log entry associated with a dataset.
    Adds the current timestamp and links to the dataset's ObjectId.
    
    Returns:
        str: The inserted log's ID, or None if the dataset_id is invalid.
    """
    try:
        oid = ObjectId(dataset_id)
    except InvalidId:
        return None

    data.update({
        "dataset_id": oid,
        "timestamp": datetime.utcnow()
    })
    result = quality_logs_collection.insert_one(data)
    return str(result.inserted_id)


def get_quality_logs(dataset_id):
    """
    Retrieve all quality logs associated with a specific dataset.

    Returns:
        list: A list of quality log documents. Returns an empty list if dataset_id is invalid.
    """
    try:
        oid = ObjectId(dataset_id)
    except InvalidId:
        return []

    return list(quality_logs_collection.find({"dataset_id": oid}))
