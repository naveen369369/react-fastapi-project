from fastapi import FastAPI,HTTPException,Request


app=FastAPI()
ses={}
max_req=5
@app.get("/request")
def request(req:Request):
   cl_ip=req.client.host
   ses[cl_ip]=ses.get(cl_ip,0)+1
   if ses[cl_ip]>max_req:
      raise HTTPException(status_code=420,detail="Too many Request come . Your exists the limit try it after 24hrs")    
   return{
      "message":f"Request {ses.get(cl_ip)} Accepted"
   }