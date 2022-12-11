# https://dormousehole.readthedocs.io/en/latest/config.html
class EnvConfig(object):
    # mongo配置
    MONGODB_DB = "bins"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    AUTO_SALT = "c90a!DQ.poi@"
    AUTO_SECRET_KEY = "jiocasiFHIKS9231534213IKJCAISO8"
    # token时效
    AUTO_TOKEN_EXPIRES_IN = 60 * 60 * 24 * 7  # 7天过期
    # 主机监听地址
    HOST = "0.0.0.0"
    # server端口号
    PORT = 5001
    # 是否开启debug模块
    DEBUG = False
    # oss配置文件路径
    OSS_CONFIG_YAML_PATH = "/home/class-undefined/code/AcademicGarbage/server/oss.yaml"
    # redis
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
