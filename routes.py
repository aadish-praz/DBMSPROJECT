from fastapi import FastAPI, Depends
from connection import get_db
from services import CustomerServices


app = FastAPI()


@app.get("/")
def home(db = Depends(get_db)):
    res = CustomerServices.create_customer(db)
    return res