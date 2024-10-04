import json
from xml.etree.ElementTree import indent

from falcon.status_codes import HTTP_400, HTTP_200, HTTP_500

from Connection.MongoManager import insert, find
from Services.User import User


def post_service(req,res):
    try:
        inputt=req.media

        age = inputt.get("age")
        name = inputt.get("name")
        email = inputt.get("email")
        user = User(age, name, email)
        # insert("jack", {"name": user.name, "age": user.age, "email": user.email})
        if not user.validage():
            res.media = {"message": "Not a valid age"}
            res.status = HTTP_400
            return
        if not user.validname():
            res.media = {"message": "Not a valid name"}
            res.status = HTTP_400
            return
        if not user.validemail():
            res.media = {"message": "Not a valid email"}
            res.status = HTTP_400
            return
        result = find("user",{"email": email})
        result = list(result)
        if result:
            res.media = {"message": "Email id already exist"}
            res.status = HTTP_400
            return
        document={"name": user.name, "age": user.age, "email": user.email}
        insert("user",{"name": user.name, "age": user.age, "email": user.email})
        write_file(document)

        res.media = {"message": "Data inserted"}
        res.status = HTTP_200
        return
    except Exception as e:
        res.media = {"message": str(e)}
        res.status = HTTP_500
        return


def write_file(document):
    with open(r"C:\data\sample.json","r") as file:
        json_object=json.load(file)
    # print(type(json_object))
    if "data" not in json_object or not isinstance(json_object["data"], list):
        json_object["data"] = []
    json_object["data"].append(document)
    documents=json.dumps(json_object,indent=3)
    # documents=json.dumps(document,indent=3)
    with open(r"C:\data\sample.json","w") as file1:
        file1.write(documents)


def get_service(response):
    try:
        result = find("user", {})
        print(result)
        result = list(result)
        print(result)

        response.media = {"message": "Successfully fetched",
                          "data": result}
        response.status = HTTP_200
    except Exception as e:
        response.media = {"message": str(e)}
        response.status = HTTP_500

def get_email_service(request,response):
    try:
        email = request.get_param("email")
        if not email:
            response.media = {"message": "Email is necessary"}
            response.status = HTTP_400
            return
        result = find("user",{"email": email})
        # print(result)
        result = list(result)
        # print(result)
        if result:
            response.media = {"message": "Successfully fetched", "result": result}
            response.status = HTTP_200
        else:
            response.media = {"message": "User not Found"}
            response.status = HTTP_400
    except Exception as e:
        response.media = {"message": str(e)}
        response.status = HTTP_500