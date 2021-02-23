from flask_restful import Resource, reqparse
from modules.user import User


class RegisterUser(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username',
                             type=str,
                             required=True,
                             help="must be written as string type"
                             )
    user_parser.add_argument('password',
                             type=str,
                             required=True,
                             help="must be written as string type"
                             )

    def post(self):
        data = RegisterUser.user_parser.parse_args()
        user = User.find_by_username(data['username'])

        if user:
            return { "Message": "user with this name already exists" }

        user = User(**data)
        user.save_to_db()
        return { "Message": "user successfully created" }
