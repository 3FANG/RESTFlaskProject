def validate(people: dict) -> dict:
    errors = {}

    if "birthday" not in people:
        errors['birthday'] = "Не введена дата рождения"

    if 'email' not in people:
        errors['email'] = "Не введена почта"

    if 'fio' not in people:
        errors['fio'] = "Не введено ФИО"

    if 'phone' not in people:
        errors['phone'] = "Не введен номер телефона"

    return errors


def validate_update_data(people: dict) -> dict:
    allowed_parameters = [
        "birthday", "email", "phone", "fio"
    ]

    if "id" in people.keys():
        return {"primary_id": "id человека нельзя изменять"}

    if not all(map(lambda x: x in allowed_parameters, people.keys())):
        return {"invalid_parameters": "Введены невалидные параметры"}

    return {}
