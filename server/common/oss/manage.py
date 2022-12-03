from typing import Any
from app import app


class OssManage():
    def __init__(self):
        import oss2
        config = self.__read_oss_config()
        access_key_id = config["access_key_id"]
        access_key_secret = config["access_key_secret"]
        endpoint = config["endpoint"]
        bucket_name = config["bucket"]
        auth = oss2.Auth(access_key_id, access_key_secret)
        self.bucket = oss2.Bucket(auth, endpoint, bucket_name)
        self.prefix = f"https://{bucket_name}.{endpoint}"

    def __read_oss_config(self):
        import yaml
        config_path = app.config["OSS_CONFIG_YAML_PATH"]
        stream = open(config_path, "rb")
        return yaml.load(stream, yaml.SafeLoader)

    def get_object(self, filename: str) -> Any:
        """获得一个oss对象"""
        return self.bucket.get_object(filename)

    def upload(self, filename: str, data: Any, progress_callback=None):
        """上传数据至oss"""
        rst = self.bucket.put_object(filename, data, progress_callback)
        return self.get_url(filename)

    def get_url(self, filename: str) -> str:
        """获得文件下载地址"""
        return f"{self.prefix}/{filename}"


oss = OssManage()


def test():
    rst = oss.upload("foo.txt", "bar")
    assert rst == "https://bins-1.oss-cn-hangzhou.aliyuncs.com/foo.txt"
