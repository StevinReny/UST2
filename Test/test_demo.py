# from falcon import testing
# import pytest
# from falcon.status_codes import HTTP_200, HTTP_404, HTTP_500
# from mongomock.mongo_client import MongoClient
#
# # from Connection.MongoConnection import collections
# from Controller.Manager import Demo, app
#
#
# @pytest.fixture
# def client():
#     return testing.TestClient(app)
#
# @pytest.fixture
# def mongo_client():
#     client = MongoClient()
#     db = client['test']
#     collections = db['test_collection']
#     yield collections #Return collection to test
#     client.drop_database('test')
#
# # def test_on_valid_user(client,mongo_client):
# #     input={"name":"Stevin","age":12,"email":"jdjds@gmail.com"}
# #     result=client.simulate_post('/hello',json=input)
# #
# #     assert result.status==HTTP_200
# #     assert result.json=={"message":"Data inserted"}
#
#
# def test_on_valid_user(client, mongo_client):
#     input_data = {"name": "nivets", "age": 12, "email": "jdjds@gmail.com"}
#     result = client.simulate_post('/hello', json=input_data)
#
#     assert result.status == HTTP_200
#     assert result.json == {"message": "Data inserted"}
#     mongo_client.insert_one(input_data)
#     assert mongo_client.count_documents({}) == 1
#     inserted_data = mongo_client.find_one()
#
#     assert inserted_data['name'] == input_data['name']
#     assert inserted_data['age'] == input_data['age']
#     assert inserted_data['email'] == input_data['email']
#
# def test_on_invalidage(client):
#     input = {"name": "Stevin", "age": "12", "email": "jdjds@gmail.com"}
#     result = client.simulate_post('/hello', json=input)
#     assert result.status == HTTP_404
#     assert result.json == {"message": "Not a valid age"}
#
# def test_on_invalidname(client):
#     input = {"name": 12, "age": 12, "email": "jdjds@gmail.com"}
#     result = client.simulate_post('/hello', json=input)
#     assert result.status == HTTP_404
#     assert result.json == {"message": "Not a valid name"}
#
# def test_on_invalidemail(client):
#     input = {"name": 12, "age": 12, "email": "jdjdsgmail.com"}
#     result=client.simulate_post('hello',json=input)
#     assert result.status==HTTP_404
#     assert result.json=={"message":"Not a valid email"}
#
# def test_onexception(client):
#     input = {"name": "Stevin", "age": 12, "email": "jdjds@gmail.com"}
#     with pytest.raises(Exception) as e:
#         result=client.simulate_post("/hello",json=input)
#         assert result.status==HTTP_500
#         assert result.json=={"message":str(e)}
#
# def test_on_get(client,mongo_client):
