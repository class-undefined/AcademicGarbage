from server.db import mongodb
import datetime


class Photo(mongodb.EmbeddedDocument):
    original_url = mongodb.StringField(required=True)  # 原始图片url
    processed_url = mongodb.StringField(required=False) # 处理后图片url
    create_time = mongodb.DateTimeField(default=datetime.datetime.utcnow) # 创建时间
    update_time = mongodb.DateTimeField(default=datetime.datetime.utcnow) # 更新时间
    accuracy = mongodb.FloatField(max_value=1.0, required=False)  # 识别准确率
    helmets_count = mongodb.IntField(default=0)  # 图中安全帽数量
    
    