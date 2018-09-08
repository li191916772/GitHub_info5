from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config
from config import config

db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    pass

    app = Flask(__name__)

    app.config.from_object(config[config_name])
    # 配置redis
    db.init_app(app)
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # CSRFProtect只做验证工作，cookie中的 csrf_token 和表单中的 csrf_token 需要我们自己实现
    CSRFProtect(app)
    # 配置Session
    Session(app)

    # 注册index蓝图
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app