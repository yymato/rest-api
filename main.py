import base64
from io import BytesIO

import requests
from flask import Flask, make_response, jsonify, render_template
from flask_login import LoginManager

from data import db_session
from data.db_session import create_session
from data.users import User

from users_api import main_server_api
from yandex_api.static_maps_api import get_picture


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run(app.run(host='127.0.0.1', port=8080))

@app.route('/users_show/<int:user_id>')
def users_show(user_id):
    response = requests.get(f'http://localhost:29/api/users/{user_id}').json()
    print(response)
    print(get_picture(response['city']))
    if 'error' not in response.keys():
        return render_template('show_users.html', name=response['name'], city=response['city'], image=
                               base64.b64encode(BytesIO(get_picture(response['city']).content).getvalue()).decode('utf-8'))
    else:
        return '<h1>Error</h1>'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

if __name__ == '__main__':
    main()