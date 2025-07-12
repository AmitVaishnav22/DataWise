from marshmallow import Schema, fields
from datetime import datetime

class DatasetSchema(Schema):
    name = fields.Str(required=True)
    owner = fields.Str(required=True)
    description = fields.Str()
    tags = fields.List(fields.Str())
    is_deleted = fields.Bool(load_default=False)

    created_at = fields.DateTime(dump_only=True, dump_default=datetime.utcnow)
    updated_at = fields.DateTime(dump_only=True, dump_default=datetime.utcnow)


class QualityLogSchema(Schema):
    status = fields.Str(required=True)  # Should be 'PASS' or 'FAIL'
    details = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True, dump_default=datetime.utcnow)
