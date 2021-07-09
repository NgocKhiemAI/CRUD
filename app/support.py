from pydantic import BaseModel

def ResponseModel(data, message):  # Ham tra ve thong bao , vi du nhu thong bao "friend added successfully." 
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):                     # Ham thong bao loi
    return {"error": error, "code": code, "message": message}


class InforSchema(BaseModel) :     # Model de nhap vao , dung trong ham add-data, update-data
    Name  : str
    Age   : int
    Gender : str