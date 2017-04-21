import os.path

import peewee

# 配置
DATABASE = 'peewee.db'

# 创建数据库
database = peewee.SqliteDatabase(DATABASE)

class BaseModel(peewee.Model):
    class Meta:
        database = database

# 用户表
class User(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField()
    join_date = peewee.DateTimeField()
    
    class Meta:
        order_by = ('username',)

    def following(self):
        return User.select().join(
            Relationship, on=Relationship.to_user,
        ).where(Relationship.from_user == self)

    def followers(self):
        return User.select().join(
            Relationship, on=Relationship.from_user,
        ).where(Relationship.to_user == self)

    def is_following(self, user):
        return Relationship.select().where(
            (Relationship.from_user == self) &
            (Relationship.to_user == user)
        ).count() > 0

    def gravatar_url(self, size=80):
        return 'http://lorempixel.com/80/80/?' + self.username

# 关系表
class Relationship(BaseModel):
    from_user = peewee.ForeignKeyField(User, related_name='relationships')
    to_user = peewee.ForeignKeyField(User, related_name='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )

# 消息表
class Message(BaseModel):
    user = peewee.ForeignKeyField(User)
    content = peewee.TextField()
    pub_date = peewee.DateTimeField()

    class Meta:
        order_by = ('-pub_date',)

# 数据库初始化，只有于创建数据库
def create_tables():
    database.connect()
    database.create_tables([User, Relationship, Message])
    database.close()

if __name__ == '__main__':
    if os.path.isfile(DATABASE):
        create_tables()