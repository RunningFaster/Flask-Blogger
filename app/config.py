import os
# 通用配置
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    # 秘钥
    SECRET_KEY = '123456'
    # 模板文件自动加载
    TEMPLATES_AUTO_RELOAD = True
    # 数据库相关的配置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 邮件发送
    MAIL_SERVER = 'smtp.126.com'
    MAIL_USERNAME = 'ren754203791@126.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'renjing13471344'
    # 文件上传
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir,'upload')

# 配置开发环境
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'blog-dev.sqlite')

# 测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'blog-test.sqlite')

# 生产环境
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'blog.sqlite')

# 配置字典
config = {
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'product':ProductConfig,

    'default':DevelopConfig
}
