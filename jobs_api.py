import flask
from flask import jsonify

from data.db_session import create_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
)

@blueprint.route('/api/jobs')
def get_jobs():
    db_session = create_session()
    return jsonify(
        {
            'jobs': [i.to_dict() for i in db_session.query(Jobs).all()]
        }
    )