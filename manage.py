from flask_script import Manager
# 将主要配置写在包内，调用块的时候直接调用函数
from app import create_app
import os

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manage = Manager(app)

@app.route('/')
def index():
    return 'hhaha'

if __name__ == '__main__':
    manage.run()
