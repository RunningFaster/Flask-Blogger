from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import register_blueprint
# 创建一个工厂专门用来创建app
def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 初始化配置
    if config_name not in config:
        config_name = 'default'
    app.config.from_object(config[config_name])
    # 配置扩展，初始化
    config_extensions(app)
    # 蓝本注册
    register_blueprint(app)
    # 返回实例
    return app

