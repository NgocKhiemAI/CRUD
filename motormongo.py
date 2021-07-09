from fastapi import FastAPI
import uvicorn 
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
from bson.objectid import ObjectId

# mongodb 
MONGO_DETAILS = "mongodb://ngockhiem:1234@mongodb_container:27017/"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)


mydatabase = client["listfriends"]
mycollection = mydatabase["friend"]


from app.function import (
    add_friend,
    delete_friend,
    update_friend,
    friend_helper,
)

from app.support import(
    ErrorResponseModel,
    InforSchema ,
    ResponseModel, 
)
# api 

app = FastAPI()

# get all data in database 

@app.get("/")
async def retrieve_friend():
    friends = []
    async for friend in mycollection.find():
       friends.append(friend_helper(friend))
    return friends


# get data in database by id

@app.put("/id")
async def retrieve_friend_id(id: str) -> dict:
    friend = await mycollection.find_one({"_id": ObjectId(id)})
    if friend:
        return friend_helper(friend)

# Add data to database
@app.post("/add")

async def add_friend_data(friend: InforSchema = Body(...)):
    friend = jsonable_encoder(friend) # document must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument, or a type that inherits from collections 
    new_friend = await add_friend(friend)
    return ResponseModel(new_friend, "friend added successfully.")

#Update data

@app.put("/update/")

async def update_friend_data(id: str, req: InforSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_friend = await update_friend(id, req)
    if updated_friend:
        return ResponseModel(
            "friend with ID: {} name update is successful".format(id),
            "friend name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the friend data.",
    )

# Delete data 

@app.delete("/delete/")

async def delete_friend_data(id: str):
    deleted_friend = await delete_friend(id)
    if deleted_friend:
        return ResponseModel(
            "friend with ID: {} removed".format(id), "friend deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "friend with id {0} doesn't exist".format(id)
    )