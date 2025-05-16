from pony.orm import Database, Required, PrimaryKey


db = Database()

class OperationResult(db.Entity):
    id = PrimaryKey(int, auto=True)
    a = Required(int)
    b = Required(int)
    operation = Required(str)
    result = Required(int)

    class Meta:
        table = "OperationResult"

def init_db():
    db.bind(provider='postgres', user='user', password='password', host='db', database='dbname')
    db.generate_mapping(create_tables=True)