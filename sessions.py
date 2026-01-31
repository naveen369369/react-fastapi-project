from fastapi import FastAPI,Response,Cookie,HTTPException
import uuid
from typing import Optional
from datetime import datetime ,timedelta

app=FastAPI()

userName="softsuave"
upass = 'soft@123'
session={}
time=1
@app.post("/login")
def login(username: str,upass1: str,res: Response):
     if userName==username and upass==upass1:
        sid=str(uuid.uuid4())
        cur=datetime.now()
        ex=cur+timedelta(minutes=time)
        session[sid]={"UserName":username,"ex-time":ex}
        res.set_cookie(key="sid",value=sid,httponly=True,max_age=time*60)
        return{
             "message":"Sucess",
             "Time":{"cur":cur,"ex":ex}
        }
     else:
          raise HTTPException(status_code=401,detail="Invalid credatial")
     
@app.get("/home")
def home(sid: Optional[str]= Cookie(None)):
     if sid is None or sid not in session:
         raise HTTPException(status_code=401,detail="not authenticated")
     s=session[sid]
     if s["ex-time"]<datetime.now():
        session.pop(sid)
     return{
         "View": session
          }
     