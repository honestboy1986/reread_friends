from quick_orm.core import Database
from sqlalchemy import Column, String
from sqlalchemy.types import DateTime
__metaclass__ = Database.DefaultMeta

class User:
    email = Column(String(30))
    name = Column(String(30))
    password = Column(String(30))
    phonenumber = Column(String(12))
    address  = Column(String(40))
class Feed:
    email = Column(String(30))
    content = Column(String(150))
    f_time = Column(DateTime())
Database.register()


