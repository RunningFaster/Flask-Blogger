from flask import Blueprint,render_template
from app.forms import RegisterForm
user = Blueprint('user', __name__)

@user.route('/register/')
def register():
    form = RegisterForm()
    return render_template('user/register.html',form=form)


@user.route('/login/')
def login():
    return '欢迎登陆'

