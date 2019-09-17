from pymongo import MongoClient

client = MongoClient("mongodb+srv://phunq:aos159753@api-lcrp8.mongodb.net")
db = client.moneylover

test_collection = db.test
spendings_collection = db.spendings
group1_collection = db.group1
group2_collection = db.group2

group1 = [
	'Ăn uống',
	'Di chuyển',
	'Sinh hoạt',
	'Mua sắm',
	'Giải trí',
	'Chăm sóc',
	'Học tập',
	'Cho đi',
	'Khác',
]

group2 = [
	{'value': 'Mua thực phẩm', 'parent': 'Ăn uống'},
	{'value': 'Ăn ngoài', 'parent': 'Ăn uống'},
	{'value': 'Đổ xăng', 'parent': 'Di chuyển'},
	{'value': 'Mua vé|Gọi xe', 'parent': 'Di chuyển'},
	{'value': 'Tiền điện', 'parent': 'Sinh hoạt'},
	{'value': 'Tiền mạng', 'parent': 'Sinh hoạt'},
	{'value': 'Tiền nước', 'parent': 'Sinh hoạt'},
	{'value': 'Phí sinh hoạt', 'parent': 'Sinh hoạt'},
	{'value': 'Gửi xe', 'parent': 'Sinh hoạt'},
	{'value': 'Quần áo', 'parent': 'Mua sắm'},
	{'value': 'Mỹ phẩm', 'parent': 'Mua sắm'},
	{'value': 'Đồ dùng hàng ngày', 'parent': 'Mua sắm'},
	{'value': 'Xem phim', 'parent': 'Giải trí'},
	{'value': 'Chơi game', 'parent': 'Giải trí'},
	{'value': 'Khám bệnh|Mua thuốc', 'parent': 'Chăm sóc'},
	{'value': 'Mua sách', 'parent': 'Học tập'},
	{'value': 'Khóa học', 'parent': 'Học tập'},
	{'value': 'Tiền mừng', 'parent': 'Cho đi'},
	{'value': 'Tiền thăm hỏi', 'parent': 'Cho đi'},
	{'value': 'Mất tiền ngu', 'parent': 'Khác'},
]

# for group in group1:
# 	group1_collection.insert_one({'value': group})
# for group in group2:
# 	group2_collection.insert_one({'value': group['value'], 'parent': group['parent']})
