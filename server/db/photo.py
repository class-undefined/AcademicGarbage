from server.db import mongodb
from server.common.oss.manage import oss
import datetime
from typing import Dict, Tuple


class Photo(mongodb.Document):
    original_url: str = mongodb.StringField(required=True)  # 原始图片url
    processed_url: str = mongodb.StringField(required=False)  # 处理后图片url
    create_time: datetime = mongodb.DateTimeField(
        default=datetime.datetime.utcnow)  # 创建时间
    update_time: datetime = mongodb.DateTimeField(
        default=datetime.datetime.utcnow)  # 更新时间
    accuracy: float = mongodb.FloatField(
        max_value=1.0, required=False)  # 识别准确率
    helmets_count: int = mongodb.IntField(default=0)  # 图中安全帽数量
    userid: str = mongodb.StringField(required=True)  # userid

    def to_dict(self) -> Dict:
        return {
            "original_url": self.original_url,
            "processed_url": self.processed_url,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "accuracy": self.accuracy,
            "helmets_count": self.helmets_count,
            "userid": self.userid
        }

    def __str__(self) -> str:
        return str(self.to_dict())

    @staticmethod
    def query_by_id(id: str) -> Tuple["Photo", None]:
        photos = Photo.objects(id=id)
        if photos is None:
            return None
        return photos[0]

    @staticmethod
    def from_stream(stream, userid: str, filename: str) -> "Photo":
        """从stream构建Photo实例, 自动上传至oss"""
        path = f"{userid}/{filename}"
        original_url = oss.upload(path, stream)
        return Photo(original_url=original_url, userid=userid)
