from flask import Blueprint, request, jsonify
from services import dataset_service, quality_log_service
from models.schemas import DatasetSchema
from flasgger import swag_from


bp = Blueprint('datasets', __name__)
dataset_schema = DatasetSchema()

@bp.route("/datasets", methods=["POST"])
@swag_from("../docs/dataset_docs/post_dataset.yml")
def create_dataset():
    try:
        data = dataset_schema.load(request.json)
        dataset = dataset_service.create_dataset(data)
        return jsonify({"message": dataset}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/datasets", methods=["GET"])
@swag_from("../docs/dataset_docs/get_datasets.yml")
def list_datasets():
    try:
        filters = {}
        owner = request.args.get("owner")
        tag = request.args.get("tag")
        if owner:
            filters["owner"] = owner
        if tag:
            filters["tags"] = tag
        datasets = dataset_service.get_datasets(filters)
        for d in datasets:
            d["_id"] = str(d["_id"])
        return jsonify(datasets)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/datasets/<id>", methods=["GET"])
@swag_from("../docs/dataset_docs/get_dataset_by_id.yml")
def get_dataset(id):
    try:
        dataset = dataset_service.get_dataset_by_id(id)
        if not dataset:
            return jsonify({"error": "Not found"}), 404
        dataset["_id"] = str(dataset["_id"])
        return jsonify(dataset)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/datasets/<id>", methods=["PUT"])
@swag_from("../docs/dataset_docs/put_dataset.yml")
def update_dataset(id):
    try:
        data = request.json
        modified = dataset_service.update_dataset(id, data)
        return jsonify({"modified": modified})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/datasets/<id>", methods=["DELETE"])
@swag_from("../docs/dataset_docs/delete_dataset.yml")
def soft_delete(id):
    try:
        result = dataset_service.delete_dataset(id)
        return jsonify({"deleted": result.modified_count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

