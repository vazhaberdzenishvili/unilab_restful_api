from db import db


class itemModel(db.Model):
    __tablename__ = "store"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    price = db.Column(db.Float(5))
    quantity = db.Column(db.Float(precision=2))

    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def json(self):
        return { "ID":self.id, "name": self.name, "price": self.price, "quantity": self.quantity }

    @classmethod
    def get_all(cls):
        return { "items": list(map(lambda item: item.json(), cls.query.all())) }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
