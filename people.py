import json

from flask import request, abort, make_response

from config import db
from services import validate, validate_update_data
from models import Person, people_schema, person_schema


def get_peoples():
    people = Person.query.all()

    return people_schema.dump(people)


def get_people_by_id(people_id: str):
    person = Person.query.filter(Person.id == int(people_id)).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with id {people_id} not found")


def create_people(people: dict):
    errors = validate(people)

    if errors:
        return {"code": 422, "errors": errors}, 422

    new_people = person_schema.load(people, session=db.session)

    db.session.add(new_people)
    db.session.commit()

    return person_schema.dump(new_people), 201


def update_people(people_id: str, people: dict):
    existing_people = Person.query.filter(Person.id == int(people_id)).one_or_none()

    if existing_people is None:
        return abort(404, f"Person with id {people_id} not found")

    errors = validate_update_data(people)

    if errors:
        return {"code": 422, "errors": errors}, 422

    updated_people = person_schema.load(people, session=db.session)
    updated_people.id = existing_people.id

    db.session.merge(updated_people)
    db.session.commit()

    updated_people = Person.query.filter(Person.id == int(people_id)).one_or_none()

    return person_schema.dump(updated_people), 201


def delete_people(people_id: str):
    existing_person = Person.query.filter(Person.id == int(people_id)).one_or_none()

    if existing_person is None:
        return abort(404, f"Person with id {people_id} not found")

    db.session.delete(existing_person)
    db.session.commit()

    return make_response(f"{existing_person.fio} successfully deleted", 200)
