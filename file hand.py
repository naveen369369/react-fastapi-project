from fastapi import FastAPI ,UploadFile,File
from pydantic import BaseModel 
from typing import List
import pandas as pd
from PyPDF2 import PdfReader
import io
app=FastAPI()

#For single file storing and read both excel and pdf file Only

@app.post("/fileUpload")
async def fileupload(fileUp: UploadFile=File(...)):
 
    text=await fileUp.read()
    name=fileUp.filename.lower()
# for read the excel file
    if name.endswith((".xls",".xlsx")):
        df=pd.read_excel(io.BytesIO(text))
        return{
            "Type":"Excel",
            "Preview":df.head(2).to_dict()
        }
    #For read the pdf file
    elif name.endswith(".pdf"):
        con=PdfReader(io.BytesIO(text))
        text1="".join([p.extract_text() or "" for p in con.pages[:29]])
        return{
            "Type":"PDF",
            "Preview":text1,
            "PDF Page Size":len(con.pages),
            "Total Words Length":len(text1),
            "Total Nullam Words": text1.count("Nullam")
        }
    return{
        "Error":"Unsupport File Format"
    }

#For multiple file storing and read only text file Only

# class items(BaseModel):
#     name: str =  Field(min_length=3,max_length=50,pattern="^[a-zA-Z]+$")
#     age: int = Field(gt=18,lt=35)
#     status: Optional[bool] = None


# @app.post("/fileUpload")
# async def fileupload(fileUp: List[UploadFile]=File(...)):
#     result=[]
#     for f in fileUp:

#      text= await f.read()

#      try:
#         text_p=text.decode("utf-8")[:200]

#      except:
#         text_p="No Data Found"

#      result.append({
#         "File Name ":f.filename,
#         "File Type ":f.content_type,
#         "File Size ":len(text),
#         "Text ":text_p
#     })
#     return result
