from flask import current_app, render_template
from app.extensions import mail
from flask_mail import Message
from threading import Thread

def async_send_mail(app, msg):
    # 邮件发送需要在程序上下文中进行，
    # 新的线程中没有上下文，需要手动创建
    with app.app_context():
        mail.send(msg)
    print('成功发送')

# 封装函数发送邮件
def send_mail(subject, to, template, **kwargs):
    # 从代理中获取代理的原始对象
    app = current_app._get_current_object()
    # 创建用于发送的邮件消息对象
    msg = Message(subject=subject, recipients=[to],
                  sender=app.config['MAIL_USERNAME'])
    # 设置内容
    msg.html = render_template('email/' + template, **kwargs)
    # 发送邮件
    # mail.send(msg)
    thr = Thread(target=async_send_mail, args=[app, msg])
    thr.start()
    return thr
