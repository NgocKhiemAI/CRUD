from fastapi import FastAPI
import uvicorn 
import pymongo 
from bson.json_util import dumps
myclient = pymongo.MongoClient("mongodb://ngockhiem:1234@mongodb_container:27017/")

mydb = myclient["listfriends"]

app = FastAPI()

@app.get("/")
async def get():
    mycol = mydb["friend"]

    x = mycol.find()
    
    return dumps(x, indent=2) 

    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)