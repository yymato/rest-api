from flask import Flask, make_response, jsonify
from flask_login import LoginManager

import users_api
from data import db_session
from data.users import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('123.sqlite')
    app.register_blueprint(jobs_api.blueprint)
    # db_sess = create_session()
    # user = User()
    # user.email = 'admin@admin.com'
    # user.name = 'admin'
    # user.set_password('123')
    # db_sess.add(user)
    # db_sess.commit()
    app.run()


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