from bson import ObjectId
from flask import jsonify
from flask_restful import Resource, reqparse

from db import spendings_collection, group1_collection, group2_collection
from common.utils import str2dt


class Spendings(Resource):
	def __init__(self):
		group1 = group1_collection.find().distinct('value')
		group2 = group2_collection.find().distinct('value')
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('amount', type=float, required=True)
		self.reqparse.add_argument('group1', choices=group1, type=str, required=True)
		self.reqparse.add_argument('group2', choices=group2, type=str, required=True)
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
			'group1': args.group1,
			'group2': args.group2,
			'detail': args.detail,
			'date'  : args.date,
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
			'group1': args.group1,
			'group' : args.group2,
			'detail': args.detail,
			'date'  : args.date,
			'wallet': args.wallet,
		}
		spendings_collection.update_one({'_id': ObjectId(_id)}, {'$set': spending})
		return {'result': 1}, 201

	def delete(self, _id):
		spendings_collection.delete_one({'_id': ObjectId(_id)})
		return {'result': 1}, 201

