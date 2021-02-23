from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.store import itemModel


class itemList(Resource):

    def get(self):
        return itemModel.get_all()


class items(Resource):
    item_parser = reqparse.RequestParser()

    item_parser.add_argument('name',
                             type=str,
                             required=True,
                             help="must be written as string type"
                             )
    item_parser.add_argument('price',
                             type=float,
                             required=True,
                             help="must be written as float type"
                             )
    item_parser.add_argument('quantity',
                             type=float,
                             required=True,
                             help="must be written as float type"
                             )

    @jwt_required()
    def get(self, name):
        item = itemModel.find_by_name(name)
        if item:
            return item.json()
        return "item doesn't exists"

    @jwt_required()
    def post(self, name):
        if itemModel.find_by_name(name):
            return "an item with this name already exists"
        data = items.item_parser.parse_args()
        item = itemModel(data['name'], data['price'], data['quantity'])
        try:
            item.save_to_db()
        except Exception as err:
            return { "message": "an error occurred inserting an item.", "error": err }, 500
        return { "Message": "item successfully added to the list" }

    @jwt_required()
    def delete(self, name):
        item = itemModel.find_by_name(name)

        if item:
            item.delete_from_db()
            return "item successfully deleted"
        else:
            return "item with this name doesn't exists"

    @jwt_required()
    def put(self, name):
        item = itemModel.find_by_name(name)
        data = items.item_parser.parse_args()

        if item:
            item.name = data["name"]
            item.price = data["price"]
            item.quantity = data["quantity"]
            item.save_to_db()
            return "an item successfully updated"
        item = itemModel(**data)
        item.save_to_db()
        return "an item successfully created"
