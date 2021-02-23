from flask import Flask, redirect
from flask_restful import Api
from resources.store import itemList, items
from flask_jwt import JWT
from security import authentication, identity
from resources.user import RegisterUser

app = Flask(__name__)
app.secret_key = "python"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def home():
    return redirect("https://github.com/vazhaberdzenishvili/unilab_restful_api/tree/main"), 302


api = Api(app)
jwt = JWT(app, authentication, identity)

api.add_resource(RegisterUser, "/registration")
api.add_resource(itemList, "/menu")
api.add_resource(items, '/menu/<string:name>')

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=6789, debug=True)
