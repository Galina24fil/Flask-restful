from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from data import users_resources
from data import db_session

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    # для списка объектов
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<users_id>')
    app.run()


if __name__ == '__main__':
    main()
