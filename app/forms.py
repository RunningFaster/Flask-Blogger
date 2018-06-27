from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email

# 用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Length(6,20,'用户名必须在6-20个字符之间')])
    password = PasswordField('密码',validators=[Length(6,20,'用户名必须在6-20个字符之间')])
    confirm = PasswordField('确认密码',validators=[EqualTo('password','两次密码不一致')])
    email = StringField('邮箱',validators=[Email('邮箱格式不正确')])
    submit = SubmitField('注册')