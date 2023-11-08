from api.common import db
from api.schema import BaseSchema


def insert_fake_data(schema: BaseSchema, data: list[dict]):
    for row in data:
        row_model = schema.load(row, session=db.session)
        db.session.add(row_model)
        db.session.commit()
