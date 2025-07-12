from flask import Blueprint, request, jsonify
from services import quality_log_service
from models.schemas import QualityLogSchema

quality_bp = Blueprint('quality_logs', __name__)
quality_log_schema = QualityLogSchema()

@quality_bp.route("/datasets/<id>/quality", methods=["POST"])
def add_quality_log(id):
    try:
        data = quality_log_schema.load(request.json)
        log_id = quality_log_service.add_quality_log(id, data)
        return jsonify({"log_id": log_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@quality_bp.route("/datasets/<id>/quality", methods=["GET"])
def get_quality_logs(id):
    try:
        logs = quality_log_service.get_quality_logs(id)
        for log in logs:
            log["_id"] = str(log["_id"])
            log["dataset_id"] = str(log["dataset_id"])
        return jsonify(logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500