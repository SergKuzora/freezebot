"""
Настройки для API
"""
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек для API
    """
    main_url: str = os.getenv('MAIN_URL', default='/')

settings = Settings()
