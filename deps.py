from database import SessionLocal #“A machine that creates DB connections”

def get_db():
    db = SessionLocal() #Creates one database session
    try:
        yield db #“Pause this function here, give db to FastAPI, and continue later.”
    finally:
        db.close()