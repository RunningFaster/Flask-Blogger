# 导入类库
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment

# 创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
moment = Moment()

# 初始化
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)