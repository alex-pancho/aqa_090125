import time

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from logger import logger

base = declarative_base()
DB_URL = "postgresql://test_user:test_password@db:5432/test_db"

engine = create_engine(DB_URL, echo=True)


class Calculation(base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    result = Column(Integer)


class PostgresSqlSession:
    def __init__(self):
        # Retry логіка
        for attempt in range(10):
            try:
                self.engine = create_engine(DB_URL, echo=True)
                # Перевірка підключення
                with self.engine.connect() as conn:
                    pass
                break
            except OperationalError as e:
                logger.error(f"[Attempt {attempt + 1}/10] DB not ready yet: {e}")
                time.sleep(2)
        else:
            raise Exception("Could not connect to the database after 10 attempts")

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        base.metadata.create_all(self.engine)

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()

        self.session.close()


def calculate_and_store(op: str, a: int, b: int):
    with PostgresSqlSession() as session:
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        else:
            raise ValueError("Unsupported operation")
        calc = Calculation(operation=op, result=result)
        session.add(calc)
        session.commit()
        return result


def delete_result():
    with PostgresSqlSession() as session:
        results = session.query(Calculation).all()

        if not results:
            return False

        for item in results:
            session.delete(item)

        session.commit()
        return True


def get_result(result):
    with PostgresSqlSession() as session:
        result = session.query(Calculation).filter_by(result=result).first()
        if not result:
            return False

        return result.result


def update_data(old_result, a, b, op):
    with PostgresSqlSession() as session:
        data = session.query(Calculation).filter_by(result=old_result).first()

        if not data:
            return False

        if op == "add":
            data.result = a + b
        elif op == "sub":
            data.result = a - b
        else:
            raise ValueError("Unsupported operation")

        data.operation = op
        session.commit()
        return data.result
