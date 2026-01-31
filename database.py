from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:VImWVtrdIYgDaqVMrHBsXlZXpFDQUpfx@tramway.proxy.rlwy.net:22237/fastapi_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,        # shows SQL queries in terminal
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()