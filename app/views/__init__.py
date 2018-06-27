from .main import main
from .user import user

# 有两个参数，一个是注册的蓝本，一个是路由的前缀
CONFIG_BLUEPRINT = (
    (main, ''),
    (user, '/user'),
)

# 注册蓝本函数
def register_blueprint(app):
    for blueprint, url_prefix in CONFIG_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=url_prefix)