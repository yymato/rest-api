import flask
from flask import jsonify, make_response

from data.db_session import create_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
)

@blueprint.route('/api/job/<int:job_id>')
def get_job(job_id):
    db_session = create_session()
    job = db_session.query(Jobs).get(job_id)
    if job:
        return jsonify({'Job': job.to_dict()})
    else:
        return make_response(jsonify({'error': 'Job not found'}, 404))


@blueprint.route('/api/jobs')
def get_jobs():
    db_session = create_session()
    return jsonify(
        {
            'Jobs': [i.to_dict() for i in db_session.query(Jobs).all()]
        }
    )

@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)