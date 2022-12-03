# https://dormousehole.readthedocs.io/en/latest/config.html
class EnvConfig(object):
    MONGODB_DB = "bins"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    AUTO_SALT = "c90a!DQ.poi@"
    AUTO_SECRET_KEY = "jiocasiFHIKS9231534213IKJCAISO8"
    AUTO_TOKEN_EXPIRES_IN = 60 * 60 * 24 * 7  # 7天过期
    HOST = "127.0.0.1"
    PORT = 5001
    DEBUG = True
    OSS_CONFIG_YAML_PATH = "/Users/class-undefined/code/projects/AcademicGarbage/server/oss.yaml"
