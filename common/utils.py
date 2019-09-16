from bson import ObjectId
import datetime
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter


class MongoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return super().default(obj)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

def str2dt(obj):
    return datetime.datetime.strptime(obj, '%d/%m/%Y')