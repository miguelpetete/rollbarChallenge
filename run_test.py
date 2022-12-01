import pytest, json

from flaskblog.routes import delete_one_item_by_id
from flaskblog import app


def test_delete_one_item_by_id()->None:
    assert delete_one_item_by_id() == None


def test_get_all_items()->None:
    response = app.test_client().get('/items')
    res =  json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert res["err"] == 0
    assert type(res["result"]["items"]) is list


def test_create_new_item()->None:
    response = app.test_client().post('/items')
    res =  json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert res["err"] == 0


def test_get_one_item_by_id()->None:
    response = app.test_client().get('/items/1349332459')
    res =  json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert res["err"] == 0
    assert res["result"]["id"] == 1349332459


def test_update_one_item_by_id()->None:
    response = app.test_client().patch('/items/1349332459')
    res =  json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert res["err"] == 0


def test_post_in_db()->None:
    response = app.test_client().get('/reports')
    res =  json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert res["err"] == 0
    assert type(res["result"]) is list


def test_delete_from_db()->None:
    response = app.test_client().delete('/reports')
    res =  response.data.decode('utf-8')

    assert type(res) is str 