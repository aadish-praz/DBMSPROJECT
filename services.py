from sqlalchemy import text
from sqlalchemy.orm import session
from models import CustomerCreateSchema

class CustomerServices:
    @staticmethod
    def create_customer(db: session):
        res = db.exc(
            text(
                "show tables;"
            )
        )
        
        return res