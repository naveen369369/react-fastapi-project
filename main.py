from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from deps import get_db
from database import engine, SessionLocal, Base
from model import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    # ✅ Create tables automatically
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    # ✅ Check if data already exists (IMPORTANT)
    user_count = db.query(User).count()

    if user_count == 0:
        users = [
            User(name="Naveen Kumar", email="naveen@gmail.com"),
            User(name="Rahul Sharma", email="rahul@gmail.com"),
            User(name="Anita Singh", email="anita@gmail.com")
        ]
        db.add_all(users)
        db.commit()

    db.close()
@app.get("/view")
def view(db: Session=Depends(get_db)):
   db_pro=db.query(User).all()
   return db_pro

@app.post("/create")
def create(name:str, email:str ,db: Session=Depends(get_db)):
    user=User(name=name,email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return{"meassage":"Inserted Values Sucessfull"}

@app.put("/update/{id}")
def update(id:int,name:str,email:str,db:Session=Depends(get_db)):
        
    user=db.query(User).filter(User.id==id).first()
    user.name=name
    user.email=email

    db.commit()
    db.refresh(user)
    return{"Message":"Data Updated Sucessfully"}

@app.delete("/delete/{id}")
def dele(id:str,db:Session=Depends(get_db)):
    
    user=db.query(User).filter(User.id==id).first()
    
    if not user:
        return " 404 User not Found"
    db.delete(user)
    db.commit()
    return{"message":"Deleted sucessfully"}