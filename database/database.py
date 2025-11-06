from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (AsyncAttrs, 
                                    async_sessionmaker, 
                                    create_async_engine)
from pathlib import Path

from config import settings

import pkgutil
import importlib

engine = create_async_engine(url=settings.DB_URL_asyncpg)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    
    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {", ".join(cols)}>"

def import_models():
    """
    Imports all modules in the database.models package so that 
    the classes are included in Base.metadata
    """
    pkg = "database.models"
    pkg_path = Path(__file__).with_name("models")
    for m in pkgutil.iter_modules([str(pkg_path)]):
        importlib.import_module(f"{pkg}.{m.name}")

async def async_main():
    async with engine.begin() as bgn:
        import_models()
        await bgn.run_sync(Base.metadata.create_all)