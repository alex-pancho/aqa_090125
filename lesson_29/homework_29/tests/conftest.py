import pytest
from pony.orm import db_session
from app.db import db, OperationResult


@pytest.fixture(scope="module", autouse=True)
def clear_db():
    with db_session:
        OperationResult.select().delete()

        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("ALTER SEQUENCE OperationResult_id_seq RESTART WITH 1;")
        connection.commit()