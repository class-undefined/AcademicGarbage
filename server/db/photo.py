from server.db import mongodb
import datetime
from typing import Dict


class Photo(mongodb.EmbeddedDocument):
    original_url: str = mongodb.StringField(required=True)  # 原始图片url
    processed_url: str = mongodb.StringField(required=False)  # 处理后图片url
    create_time: datetime = mongodb.DateTimeField(
        default=datetime.datetime.utcnow)  # 创建时间
    update_time: datetime = mongodb.DateTimeField(
        default=datetime.datetime.utcnow)  # 更新时间
    accuracy: float = mongodb.FloatField(max_value=1.0, required=False)  # 识别准确率
    helmets_count: int = mongodb.IntField(default=0)  # 图中安全帽数量

    def to_dict(self) -> Dict:
        return {
            "original_url": self.original_url,
            "processed_url": self.processed_url,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "accuracy": self.accuracy,
            "helmets_count": self.helmets_count
        }

    def __str__(self) -> str:
        return str(self.to_dict())
