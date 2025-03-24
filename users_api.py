import flask
import requests
from flask import jsonify, make_response
from flask import request

from data.db_session import create_session
from data.users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
)


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(users_id):
    db_session = create_session()
    user = db_session.query(User).get(users_id)
    if user:
        return jsonify({'User': user.to_dict()})
    else:
        return make_response(jsonify({'error': 'user not found'}, 404))


@blueprint.route('/api/users', methods=['GET'])
def get_all_users():
    db_session = create_session()
    return jsonify({'users': [i.to_dict() for i in db_session.query(User).all()]})


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    db_session = create_session()

    if all([key in request.json for key in
            ['name', 'about', 'work_size', 'email', 'password']]):

        user = User()
        for key in request.json.keys():
            if key != 'password':
                setattr(user, key, request.json[key])

        user.set_password(request.json['password'])
        db_session.add(user)
        db_session.commit()
        return jsonify({'id': user.id})
    else:
        return make_response(jsonify({'error': 'Bad request'}), 404)


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_user(users_id):
    db_session = create_session()
    user = db_session.query(User).get(users_id)
    if user:
        db_session.delete(user)
        db_session.commit()
        return jsonify({'success': True})
    else:
        return make_response(jsonify({'error': 'user not found'}, 404))

@blueprint.route('/api/users/', methods=['PUT'])
def edit_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    db_session = create_session()
    if 'id' in request.json.keys() and request.json['id'] and db_session.query(User).get(request.json['id']):
        user = db_session.query(User).get(request.json['id'])
        for key in request.json.keys():
            if key not in ['password', 'created_date']:
                setattr(user, key, request.json[key])

        if 'password' in request.json.keys():
            user.set_password(request.json['password'])
        db_session.commit()
        return jsonify({'success': True})
    else:
        return make_response(jsonify({'error': 'id not in request'}), 400)

@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
