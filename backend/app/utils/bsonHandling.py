from datetime import datetime

from bson import ObjectId
from flask.json.provider import DefaultJSONProvider

# bson import may appear as an error, however is already included as part of the pymongo library


"""
Overrides default JSON serialization behavior
better translates ObjectId and datetime types which are MONGO related objects to JSON
which are not natively supported by JSON.
Serves as a repeatable way to handle these types in JSON serialization.
"""


class MongoJSONProvider(DefaultJSONProvider):
    """
    Overrides the default JSON serialization behavior to handle ObjectId and datetime types.
    Using basedpyright language server shows default function as an error however including
    @staticmethod resolves the issue though, probably since default is already present within DefaultJSONProvider.
    """

    @staticmethod
    def default(obj):
        # Handle ObjectID from MongoDB t JSON string
        if isinstance(obj, ObjectId):
            return str(obj)
        # Handles datetime like above but with ISO format which is a standard JSON datetime format
        if isinstance(obj, datetime):
            return obj.isoformat()

        return DefaultJSONProvider.default(obj)
