from falcon import testing
import pytest
from falcon.status_codes import HTTP_200, HTTP_404, HTTP_500

# from Connection.MongoConnection import collections
from Controller.Controller import Demo, app


@pytest.fixture
def client():
    return testing.TestClient(app)




def test_on_valid_user(client,mongo_client):
    input={"name":"Stevin","age":12,"email":"jdjds@gmail.com"}
    result=client.simulate_post('/hello',json=input)

    assert result.status==HTTP_200
    assert result.json=={"message":"Data inserted"}

def test_on_invalidage(client):
    input = {"name": "Stevin", "age": "12", "email": "jdjds@gmail.com"}
    result = client.simulate_post('/hello', json=input)
    assert result.status == HTTP_404
    assert result.json == {"message": "Not a valid age"}

def test_on_invalidname(client):
    input = {"name": 12, "age": 12, "email": "jdjds@gmail.com"}
    result = client.simulate_post('/hello', json=input)
    assert result.status == HTTP_404
    assert result.json == {"message": "Not a valid name"}

def test_on_invalidemail(client):
    input = {"name": 12, "age": 12, "email": "jdjdsgmail.com"}
    result=client.simulate_post('hello',json=input)
    assert result.status==HTTP_404
    assert result.json=={"message":"Not a valid email"}

def test_onexception(client):
    input = {"name": "Stevin", "age": 12, "email": "jdjds@gmail.com"}
    with pytest.raises(Exception) as e:
        result=client.simulate_post("/hello",json=input)
        assert result.status==HTTP_500
        assert result.json=={"message":str(e)}

