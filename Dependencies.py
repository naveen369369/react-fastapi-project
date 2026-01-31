from fastapi import FastAPI,Depends

app=FastAPI()

#Function Dependency

# def dp():
#     return "Connected"

# @app.get('/dis')
# def dis(id:int,a:dict=Depends(dp)):
#     return{
#         "Message":"Recieved",
#         "Status":a,
#         "id":id
#     }
#-------------------------------

# Class Level Dependency

# class User():
#     def __init__(self):
#         self.name="Naveen"
#         self.age=21
#         self.place="Karur"

# def dp():
#    return User()
    
# @app.get("/disuser")
# def disuse(a:User=Depends(dp)):
#      return{
#          "Name":a.name,
#          "Age":a.age,
#          "Place":a.place
#      }
#---------------------------------

#Global Level 

# def check_tok(tok:str="123"):
#     if tok !="123":
#         raise Exception("Invalid Token")
#     return{"Message": True}

# app=FastAPI(dependencies=[Depends(check_tok)])

# @app.get("/globe")
# def globe():
#     return{
#         "Message":"Recived"
#     }

#-----------------------------------

#Sub Level Dependency - It act as Mutliple Inheritance type

# def gp(): #Grandparent
#     return{"Message":"Grand Parent"}

# def p(a:str=Depends(gp)): #Parent
#     return{"Message":"parent","super":a}

# @app.get("/sub") 
# def sub(b:str=Depends(p)): #Child
#     return{"Message":b}

#-------------------------------------
