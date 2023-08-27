"""
main.py file
"""
from fastapi import FastAPI
from pydantic import BaseModel

from .settings import settings


app = FastAPI()


class CommercialOffer(BaseModel):
    """
    Коммерческое предложение
    """
    status: str = 'ok'

@app.get(settings.main_url)
async def show_offers():
    """
    Домашняя страница
    """
    return CommercialOffer()

@app.post('/add_offer')
async def add_offer():
    """
    Добавить коммерческое предложение
    """
    return CommercialOffer()
