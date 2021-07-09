import motor.motor_asyncio
from bson.objectid import ObjectId

# mongodb 

MONGO_DETAILS = "mongodb://ngockhiem:1234@mongodb_container:27017/"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)


mydatabase = client["listfriends"]        # khai bao database
mycollection = mydatabase["friend"]       # khai bao collection
 
# Nhung thong tin can lay ra
def friend_helper(friend) -> dict:
    return {
        "id": str(friend["_id"]),
        "Name": friend["Name"],
        "Age": friend["Age"],
        "Gender": str(friend["Gender"])
    }

 # function for add data

async def add_friend(friend_data: dict) -> dict:
    friend = await mycollection.insert_one(friend_data)
    new_friend = await mycollection.find_one({"_id": friend.inserted_id})
    return friend_helper(new_friend)

# function for update data 

async def update_friend(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    friend = await mycollection.find_one({"_id": ObjectId(id)})
    if friend:
        updated_friend = await mycollection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_friend:
            return True
        return False

# function for delete data 

async def delete_friend(id: str):
   
    friend = await mycollection.find_one({"_id": ObjectId(id)})
    if friend:
        await mycollection.delete_one({"_id": ObjectId(id)})
        return True
