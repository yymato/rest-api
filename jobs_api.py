import flask
from flask import jsonify, make_response

from data.db_session import create_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
)

@blueprint.route('/api/jobs<int:job>')
def get_jobs(job_id):
    db_session = create_session()
    job = db_session.query(Jobs).get(job_id)
    if job:
        return jsonify({'job': job.to_dict()})
    else:
        return make_response(jsonify({'error': 'Job not found'}, 404))
