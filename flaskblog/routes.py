import requests
from flask import render_template, jsonify
from flaskblog import app, db
from flaskblog.function import postgres_test
from dotenv import dotenv_values
from random import randint
from flaskblog.models import Report

config = dotenv_values(".env")

url_base = "https://api.rollbar.com/api/1/"

message_global = 'Item by default '

@app.route("/")
def init():
    return render_template('/flaskblog/init.html')


@app.route("/check")
def check():
    test = postgres_test()
    if test:
        data = {
            "status" : "OK"
        }
    else: 
        data = {
            "status" : "KO"
        }
    return jsonify(data)


@app.route("/items", methods=['GET'])
def get_all_items():
    url = url_base + "items"
    headers = {
        "accept": "application/json",
        "X-Rollbar-Access-Token": config["READ_ROLLBAR"]
    }
    response = requests.get(url, headers=headers)
    return response.text


@app.route("/items/<int:id>", methods=['GET'])
def get_one_item_by_id(id):
    url = url_base + f"item/{id}"
    headers = {"X-Rollbar-Access-Token": config["READ_ROLLBAR"]}
    response = requests.get(url, headers=headers)
    return response.text


@app.route("/items", methods=['POST'])
def create_new_item(message=message_global):
    url = url_base + "item/"
    payload = {"data": {
            "environment": "development",
            "body": {"message": {"body": message + f"{randint(0,10)}"}}
        }}
    headers = {
        "accept": "application/json",
        "X-Rollbar-Access-Token": config["post_server_rollbar"],
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text


@app.route("/items/<int:id>", methods=['PATCH'])
def update_one_item_by_id(id):
    url = url_base + f"item/{id}"
    payload = {"title": message_global + f"{randint(0,10)}"}
    headers = {
        "accept": "application/json",
        "X-Rollbar-Access-Token": config["WRITTEN_ROLLBAR"],
        "content-type": "application/json"
    }
    response = requests.patch(url, json=payload, headers=headers)
    return response.text


@app.route("/items/<int:id>", methods=['DELETE'])
def delete_one_item_by_id():
    return None



@app.route("/reports", methods=['GET'])
def post_in_db():
    query = Report.query.first()
    if query == None:
        url = url_base + "reports/top_active_items?hours=24"
        headers = {
            "accept": "application/json",
            "X-Rollbar-Access-Token": config["READ_ROLLBAR"]
        }
        response = requests.get(url, headers=headers)
        rep = Report(json=response.json())
        db.session.add(rep)
        db.session.commit()
        return response.text
    else: 
        response = Report.query.first()
    return response.json
    
@app.route("/reports", methods=['DELETE'])
def delete_from_db():
    query = Report.query.first()
    if query:
        db.session.delete(query)
        db.session.commit()
        return "Deleted from database."
    else: 
        return "Empty database. Nothing to delete"
