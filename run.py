from flask import Flask
from flask_restful import Api

from common.utils import MongoJSONEncoder
from resources import (
	Test,
	Spendings,
	Spending,
)

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder
api = Api(app)
api.add_resource(Test, '/api/test')
api.add_resource(Spendings, '/api/spendings')
api.add_resource(Spending, '/api/spending/<string:_id>')


if __name__ == '__main__':
    app.run(
    	debug=True
    )