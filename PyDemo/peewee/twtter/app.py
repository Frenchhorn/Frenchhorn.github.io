import datetime

from hashlib import md5
from functools import wraps

import flask
import peewee

# config - aside from database, the rest is for use by Flask
DATABASE = 'peewee.db'
DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'

# create a flask application - this ``app`` object will be used to handle
# inbound requests, routing them to the proper 'view' functions, etc
app = flask.Flask(__name__)
app.config.from_object(__name__)

# create a peewee database instance -- our models will use this database to
# persist information
database = peewee.SqliteDatabase(DATABASE)

# base model class
class BaseModel(peewee.Model):
    class Meta:
        database = database
        
# the user model specifies its fields or columns declaratively
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
        
class Relationship(BaseModel):
    from_user = peewee.ForeignKeyField(User, related_name='relationships')
    to_user = peewee.ForeignKeyField(User, related_name='related_to')
    
    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )

class Message(BaseModel):
    user = peewee.ForeignKeyField(User)
    content = peewee.TextField()
    pub_date = peewee.DateTimeField()
    
    class Meta:
        order_by = ('-pub_date',)

def create_tables():
    database.connect()
    database.create_tables([User, Relationship, Message])

def get_current_user():
    if flask.session.get('logged_in'):
        return User.get(User.id == flask.session['logged_in'])
    else:
        raise AssertionError('No logged_in session')

def object_list():
    pass

@app.route('/')
def homepage():
    if flask.session.get('logged_in'):
        return private_timeline()
    else:
        return public_timeline()

@app.route('/private/')
def private_timeline():
    user = get_current_user()
    messages = Message.select().where(Message.user << user.following())
    return object_list('private_message.html', messages, 'message_list')

@app.route('/public/')
def public_timeline():
    pass

@app.route('/<name>')
def hello(name='world'):
    return 'Hello %s!'%name

if __name__ == '__main__':
    #app.run()
    pass
