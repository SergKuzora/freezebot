"""
main.py file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .settings import settings


app = FastAPI()

origins = [
    'https://climate-bot.netlify.app',
    'http://localhost:3000',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
async def add_offer(answ):
    """
    Добавить коммерческое предложение
    """
    return answ
