from flask import Flask
from flask_restful import Api

from resources import (
	Test,
)

app = Flask(__name__)
api = Api(app)
api.add_resource(Test, '/api/test')


if __name__ == '__main__':
    app.run(
    	debug=True,
    	port=5003,
    )