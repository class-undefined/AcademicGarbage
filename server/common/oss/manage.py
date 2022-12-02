from typing import Any
import oss2
import yaml


class OssManage():
    def __init__(self):
        config = self.__read_oss_config()
        access_key_id = config["access_key_id"]
        access_key_secret = config["access_key_secret"]
        endpoint = config["endpoint"]
        bucket_name = config["bucket"]
        auth = oss2.Auth(access_key_id, access_key_secret)
        self.bucket = oss2.Bucket(auth, endpoint, bucket_name)

    def __read_oss_config(self):
        config_path = "server/common/oss/config.yaml"
        stream = open(config_path, "rb")
        return yaml.load(stream, yaml.SafeLoader)

    def get_object(self, key: str) -> Any:
        """获得一个oss对象"""
        return self.bucket.get_object(key)

    def upload(self, key: str, data: Any, progress_callback=None):
        """上传数据至oss"""
        self.bucket.put_object(key, data, progress_callback)


def test():
    oss = OssManage()
    oss.upload("foo.txt", "bar")
