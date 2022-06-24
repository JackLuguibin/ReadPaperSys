import datetime
import uuid
from peewee import *

# 数据库
db = SqliteDatabase('mydb.sqlite')


# 用户表
class User(Model):
    COMMON = 0  # 普通用户
    WORK = 1
    ADMIN = 2
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    account = CharField(unique=True, null=True)  # 账号，手机号
    password = CharField()  # 密码
    name = CharField()  # 名字
    age = IntegerField()  # 年龄
    sex = BooleanField(default=True)  # 性别
    identity = IntegerField(default=COMMON)  # 身份
    head = CharField(null=True)  # 头像
    created = DateTimeField(default=datetime.datetime.now)  # 创建时间

    class Meta:
        database = db


def create_tables():
    with db:
        print("创建数据表")
        db.create_tables([User])


def connect_database():
    if db.is_closed():
        db.connect()


def close_database():
    if not db.is_closed():
        db.close()
