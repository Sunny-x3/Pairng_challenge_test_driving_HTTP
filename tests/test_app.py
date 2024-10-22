def test_user(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john, jane, alice"

def test_user_id(web_client):
    response = web_client.get("/users/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john"

def test_create_user(web_client):
    response = web_client.post("/users", data={"username":"lewis"})
    assert response.status_code == 201
    assert response.data.decode("utf-8") == "User lewis created with id 4"

def test_update_user(web_client):
    response = web_client.put("/users/1", data={"username":"lewis"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Id 1 updated with username lewis"

def test_delete_user(web_client):
    response = web_client.delete("/users/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Message: User deleted"