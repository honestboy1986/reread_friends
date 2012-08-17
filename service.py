from models import User, Feed
from store import get_db
def insert_user(email, name, password):
    db = get_db()
    db.create_tables()
    user = User(email=email, name=name, password=password)
    db.session.add_then_commit(user)
def insert_weibo(email, content, f_time):
    db = get_db()
    db.create_tables()
    feed = Feed(email=email, content=content, f_time=f_time)
    db.session.add_then_commit(feed) 
