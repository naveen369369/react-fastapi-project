import sqlite3
from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app=FastAPI()
conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()
# cursor.execute('''
#          create table if not exists items(
#                items_id integer primary key autoincrement,
#                name text not null,
#                des text
               
#                )
#            ''')
# conn.commit()

class Item(BaseModel):
    name:str
    des:str

#---------------------------------------------------------------------
#Create Table Values Operation:

@app.post("/items/create")
def create_item(i:Item):
    try:
        cursor.execute("Insert into items(name,des) values(?,?)",(i.name,i.des))
        conn.commit()
        return{"Message":"Values Inserted Successfully"}
    except Exception as e:
        return HTTPException(status_code=406,detail=f"Invalid details{e}")

#---------------------------------------------------------------------
#Read or Show Operation:
    
@app.get("/items/read")
def read_item():
    try:
      cursor.execute("Select * from items")
      row=cursor.fetchall()
      return [{"id":i[0],"name":i[1],"des":i[2]} for i in row]
    except Exception as e:
        return HTTPException(status_code=409,detail=f"No data Found {e}")

#---------------------------------------------------------------------
#Find or Retrive Operation:
    
@app.get("/items/find")
def fin(name:str):
    try:
        cursor.execute("Select * from items Where name=?",(name,))
        row= cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404,detail="Not Found")
        return{
            "Item_Id":row[0],
            "Name":row[1],
            "Description":row[2],
        }
    except Exception as e:
        return e

#---------------------------------------------------------------------
#Update Operation:

@app.put("/items/update")
def update(item_id:int,i:Item):
   try:
       cursor.execute("Update items set name=?,des=? Where items_id=?",(i.name,i.des,item_id,))
       conn.commit()
       return {"Message":"Item Updated Sucessfully"}

   except Exception as e:
       return HTTPException(status_code=404,detail="Invalid data")

#---------------------------------------------------------------------
#Delete Operation:

@app.delete("/items/delete")
def dele(item_id: int):
   try:
       cursor.execute(
           "Select items_id from items where items_id=?",
           (item_id,)
       )
       data = cursor.fetchone()

       if data is None:
           raise HTTPException(status_code=404, detail="Invalid Id")

       cursor.execute("Delete from items Where items_id=?", (item_id,))
       conn.commit()
       return {"Message": "Item Deleted Sucessfully"}

   except Exception:
       raise HTTPException(status_code=404, detail="Invalid Id")
#------------------------------------------------------------------------