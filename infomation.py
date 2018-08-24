import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session

app = Flask(__name__)
SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"


class Config(object):
    """工程配置信息"""
    DEBUG = True
    # 数据库的配置信息

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

 # flask_session的配置信息
    SESSION_TYPE = "redis" # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True # 让 cookie 中的 session_id 被加密签名处理
    # 指定Session保存时用到时的保存对象
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT) # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400 *2 # session 的有效期，单位是秒

app.config.from_object(Config)
db = SQLAlchemy(app)
CSRFProtect(app)
Session(app)
# 初始化ｒｅｄｉｓ存储对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

@app.route('/')
def index():
    return 'index'


if __name__=="__main__":
    app.run(debug=True)