from config import db, ma


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer)
    email = db.Culumn(db.String)
    birthday = db.Column(db.String, nullable=False)


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
