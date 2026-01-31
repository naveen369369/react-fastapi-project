from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="book"
)
cursor = db.cursor(dictionary=True)

class User(BaseModel):
    F_name: str
    age: int
    place: str

@app.get("/view_user")
def view_user():
    cursor.execute("SELECT * FROM users")
    return {"Users": cursor.fetchall()}


@app.post("/create")
def create(data: User):
    try:
        cursor.execute("INSERT INTO users (F_name, age, place) VALUES (%s, %s, %s)", (data.F_name, data.age, data.place))
        db.commit()
        return {"message": "Data Created Successfully"}
    
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))
    
@app.put("/update/{id}")
def update(id:int,i:User):
    cursor.execute("Update users set F_name=%s,age=%s,place=%s Where id=%s",(i.F_name,i.age,i.place,id))
    db.commit()
    return{"message":"Data Updated Sucessfully"}

@app.delete("/delete/{id}")
def dele(id:int):
    try:
       cursor.execute("Select id from users where id=%s", (id,))
       data = cursor.fetchone()

       if data is None:
           raise HTTPException(status_code=404, detail="Invalid Id")

       cursor.execute("Delete from users where id=%s",(id,))
       db.commit()
       return{"Message":"Deleted Sucessfully"}
    
    except Exception:
          raise HTTPException(status_code=404, detail="Invalid Id")

  