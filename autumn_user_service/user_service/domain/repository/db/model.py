from autumn_user_service.config import mysql
from peewee import *
from tabnanny import verbose
from enum import unique


class Basemodel(Model):
    class Meta:
        database = mysql.DB


class User(Basemodel):
    GENDER_CHOICES = (
        ("female", "女"),
        ("male", "男")
    )

    ROLE_CHOICES = (
        (1, "普通用户"),
        (2, "管理员")
    )
    mobile = CharField(max_length=11, index=True, unique=True)
    password = CharField()
    nick_name = CharField(max_length=20, null=True)
    Head_url = CharField(max_length=200, null=True)
    birthday = DateField(null=True)
    address = CharField(max_length=200, null=True)
    desc = TextField(null=True)
    gender = CharField(max_length=6, null=True, choices=GENDER_CHOICES)
    role = IntegerField(default=1, choices=ROLE_CHOICES)


if __name__ == "__main__":
    mysql.DB.create_tables([User])
