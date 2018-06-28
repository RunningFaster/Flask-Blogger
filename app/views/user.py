from flask import Blueprint,render_template,flash,url_for,redirect,current_app, request
from app.forms import RegisterForm,LoginForm, Changepwd
from app.email import send_mail
from app.models import User
from app.extensions import db
from flask_login import login_user, current_user, logout_user, login_required


user = Blueprint('user', __name__)

'''用户注册'''
@user.route('/register/', methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 根据提交的数据创建用户的对象
        u = User(username=form.username.data,
                 password=form.password.data,
                 email=form.email.data)
        # 保存到数据库
        db.session.add(u)
        # 手动提交一次,需要用到用户的id
        db.session.commit()
        # 生成token
        token = u.generate_activate_token()
        # 发送激活邮件
        send_mail('账户激活',form.email.data,'activate.html',
                  username=form.username.data,
                  token=token)
        # 发送提示信息，消息闪烁
        flash('注册成功！请前往邮箱激活')
        return redirect(url_for('main.index'))
    return render_template('user/register.html',form=form)

'''用户激活'''
@user.route('/activate/<token>/')
def activate(token):
    if User.check_activate_token(token):
        flash('激活成功！')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败...')
        return redirect(url_for('main.index'))

'''用户登录'''
@user.route('/login/', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 根据用户名查找用户
        u = User.query.filter(User.username == form.username.data).first()
        if not u:
            flash('无效的用户名')
        elif not u.confirmed:
            flash('账户未激活，请激活后再登陆')
        elif u.verify_password(form.password.data):
            '''用户登陆时，需要调用login_user方法，让该方法知道当前是谁登陆'''
            '''login_user(user, remember=False, duration=None, force=False, fresh=True)'''
            '''login_user('登陆的用户'，'是否记住用户的登陆状态'，'记录多久')'''
            login_user(u, remember=form.remember.data)
            flash('登陆成功')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('密码错误')
    return render_template('user/login.html',form=form)

'''用户退出'''
@user.route('/logout/')
def logout():
    # 不需要传递参数，系统知道当前的用户是谁
    logout_user()
    flash('您已退出')
    return redirect(url_for('main.index'))

'''路由保护'''
@user.route('/profile/')
# 对指定的路由进行保护，使用装饰器
@login_required
def profile():
    return render_template('user/details.html')

'''修改密码'''
@user.route('/changepwd/', methods=['POST','GET'])
def changepwd():
    form = Changepwd()
    if form.validate_on_submit():
        if not current_user.verify_password(form.oldpassword.data):
            flash('原密码错误')
            return redirect(url_for('user.changepwd'))
        elif form.oldpassword.data == form.password.data:
            flash('新密码与原密码相同，密码未修改')
            return redirect(url_for('user.changepwd'))
        current_user.password = form.password.data
        db.session.add(current_user)
        flash('密码修改成功！')
        return redirect(url_for('user.changepwd'))
    return render_template('user/changepwd.html', form=form)
