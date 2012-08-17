from quick_orm.core import Database

def get_db():
    return Database('mysql://root:@localhost/test?charset=utf8')
