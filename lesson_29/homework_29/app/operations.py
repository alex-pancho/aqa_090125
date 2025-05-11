from pony.orm import *
from .db import OperationResult, init_db
import logging


logger = logging.getLogger(__name__)

init_db()

@db_session
def add_numbers(a: int, b:int):
    result = a + b
    new_record = OperationResult(a=a, b=b, operation='add', result=result)
    flush()
    logger.debug(f"Added operation: {a} + {b} = {result}, id={new_record.id}")
    return new_record.result

@db_session
def get_result_from_db(a: int, b:int, operation='add'):
    record = OperationResult.get(a=a, b=b, operation=operation)
    if record:
        logger.debug(f"Retrieved from DB: id={record.id}, {a} + {b} = {record.result}")
    else:
        logger.debug(f"No record found for: {a} + {b}")
    return record

@db_session
def delete_result_by_id(record_id: int):
    record = OperationResult.get(id=record_id)
    if record:
        record.delete()
        logger.debug(f"Deleted record with id={record_id}")
        return True
    else:
        logger.debug(f"No record found with id={record_id} to delete")
        return False
