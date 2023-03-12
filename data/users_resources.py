from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request, jsonify
from . users import User
from data import db_session
from werkzeug.security import generate_password_hash
import parser

def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")

class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        news = session.query(User).get(users_id)
        return jsonify({'users': news.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'password_hash'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        news = session.query(User).get(users_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'password_hash')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        news.password_hash = generate_password_hash(request.json['password'])
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})
