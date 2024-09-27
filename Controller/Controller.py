import json
from bson.json_util import dumps

import falcon
from falcon import HTTP_200, HTTP_404, HTTP_400, HTTP_500

from Connection.MongoConnection import collections
from Model.User import User


class Demo:

    def on_post(self,req,res):
        try:
            inputt=req.media
            age=inputt.get("age")
            name=inputt.get("name")
            email=inputt.get("email")
            user=User(age,name,email)
            if not user.validage():
                res.media = {"message": "Not a valid age"}
                res.status = HTTP_404
                return
            if not user.validname():
                res.media = {"message": "Not a valid name"}
                res.status = HTTP_404
                return
            if not user.validemail():
                res.media={"message":"Not a valid email"}
                res.status = HTTP_404
                return
            collections.insert_one({"name":user.name,"age":user.age,"email":user.email})
            res.media={"message":"Data inserted"}
            res.status=falcon.HTTP_200
        except Exception as e:
            res.media={"message":str(e)}
            res.status=HTTP_500


    def on_get(self,request,response):
        try:
            result=collections.find({},{"name":1,"age":1,"email":1,"_id":0})
            result=list(result)
            response.media={"message":"Successfully fetched",
                            "data":result}
            response.status=HTTP_200
        except Exception as e:
            response.media={"message":str(e)}
            response.status=HTTP_500

    def on_get_email(self,request,response):
        try:
            email=request.get_param("email")
            if not email:
                response.media={"message":"Email is necessary"}
                response.status=HTTP_400
                return
            result=collections.find({"email":email},{"_id":0})
            result=list(result)
            if result:
                response.media = {"message": "Successfully fetched", "result": result}
                response.status=HTTP_200
            else:
                response.media = {"message": "User not Found"}
                response.status=HTTP_404
        except Exception as e:
            response.media={"message":str(e)}

app=falcon.App()
demo=Demo()
app.add_route('/hello',demo)
app.add_route('/hello/email',demo,suffix='email')


if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    httpd.serve_forever()