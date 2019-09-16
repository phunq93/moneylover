from bson import ObjectId
from flask import jsonify
from flask_restful import Resource, reqparse

from db import spendings_collection
from common.utils import str2dt


class Spendings(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('amount', type=float, required=True)
		self.reqparse.add_argument('group', type=str, required=True)
		self.reqparse.add_argument('detail', type=str, required=True)
		self.reqparse.add_argument('date', type=str2dt, required=True)
		self.reqparse.add_argument('wallet', type=str, required=True)

	def get(self):
		spendings = spendings_collection.find()
		return jsonify(spendings)

	def post(self):
		args = self.reqparse.parse_args()
		spending = {
			'amount': args.amount,
			'group': args.group,
			'detail': args.detail,
			'date': args.date,
			'wallet': args.wallet,
		}
		spendings_collection.insert_one(spending)
		return {'result': 1}, 201


class Spending(Resource):
	def get(self, _id):
		spending = spendings_collection.find({'_id': ObjectId(_id)})
		return jsonify(spending)

	def put(self, _id):
		args = self.reqparse.parse_args()
		spending = {
			'amount': args.amount,
			'group': args.group,
			'detail': args.detail,
			'date': args.date,
			'wallet': args.wallet,
		}
		spendings_collection.update_one({'_id': ObjectId(_id)}, {'$set': spending})
		return {'result': 1}, 201

	def delete(self, _id):
		spendings_collection.delete_one({'_id': ObjectId(_id)})
		return {'result': 1}, 201

