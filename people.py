import json

from flask import request

from services import validate, validate_update_data


def get_peoples():
    with open("data.json", encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_people_by_id(people_id: str):
    with open("data.json", encoding='utf-8') as file:
        data = json.load(file)

    return data[people_id]


def create_people(people: dict):
    errors = validate(people)

    if errors:
        return {"code": 422, "errors": errors}, 422

    with open("data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

        people_id = len(data) + 1
        people["id"] = people_id

        data[str(people_id)] = people

    with open("data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return request.json, 201


def update_people(people_id: str, people: dict):
    with open("data.json", encoding='utf-8') as file:
        data = json.load(file)

    if people_id not in data.keys():
        return {"code": 404, "errors": {'bad_id': "Человек по заданному идентификатору не найден"}}, 404

    errors = validate_update_data(people)

    if errors:
        return {"code": 422, "errors": errors}, 422

    for parameter in people.keys():
        data[people_id][parameter] = people[parameter]

    with open("data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return data[people_id]


def delete_people(people_id: str):
    with open("data.json", encoding='utf-8') as file:
        data = json.load(file)

    if people_id not in data.keys():
        return {"code": 404, "errors": {'bad_id': "Человек по заданному идентификатору не найден"}}, 404

    deleted_people = data.pop(people_id)

    with open("data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return deleted_people
