from db import mongodb

import datetime
from typing import Dict, List, Tuple, Union

from common import get_oss


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
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M"),
            "accuracy": self.accuracy,
            "helmets_count": self.helmets_count,
            "userid": self.userid,
            "id": self.get_id()
        }

    def get_id(self) -> str:
        return str(self.id)

    def __str__(self) -> str:
        return str(self.to_dict())


    @staticmethod
    def query_by_id(id: str) -> Union["Photo", None]:
        photos = Photo.objects(id=id)
        if photos is None:
            return None
        return photos[0]

    @staticmethod
    def from_stream(stream, userid: str, filename: str) -> "Photo":
        """从stream构建Photo实例, 自动上传至oss"""
        path = f"{userid}/{filename}"
        original_url = get_oss().upload(path, stream)
        return Photo(original_url=original_url, userid=userid)

    @staticmethod
    def query_by_create_range(start_date: datetime.date, end_date: datetime.date, user_id: Union[str, None]=None) -> List["Photo"]:
        """查询指定日期范围创建的图片"""
        results = Photo.objects(create_time__gte=start_date, create_time__lte=end_date, userid=user_id)
        return results