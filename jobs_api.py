import flask
import requests
from flask import jsonify, make_response
from flask import request

from data.db_session import create_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
)


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_session = create_session()
    job = db_session.query(Jobs).get(job_id)
    if job:
        return jsonify({'Job': job.to_dict()})
    else:
        return make_response(jsonify({'error': 'Job not found'}, 404))


@blueprint.route('/api/jobs', methods=['GET'])
def get_all_jobs():
    db_session = create_session()
    return jsonify({'Jobs': [i.to_dict() for i in db_session.query(Jobs).all()]})


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    db_session = create_session()

    if all([key in request.json for key in
            ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']]):

        job = Jobs()
        job.team_leader = request.json['team_leader']
        job.job = request.json['job']
        job.work_size = request.json['work_size']
        job.collaborators = request.json['collaborators']
        job.is_finished = request.json['is_finished']

        db_session.add(job)
        db_session.commit()
        return jsonify({'id': job.id})
    else:
        return make_response(jsonify({'error': 'Bad request'}), 404)


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_session = create_session()
    job = db_session.query(Jobs).get(job_id)
    if job:
        db_session.delete(job)
        db_session.commit()
        return jsonify({'success': True})
    else:
        return make_response(jsonify({'error': 'Job not found'}, 404))

@blueprint.route('/api/jobs/', methods=['PUT'])
def edit_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    db_session = create_session()
    if request.json['id'] and db_session.query(Jobs).get(request.json['id']):
        job = db_session.query(Jobs).get(request.json['id'])
        for key in request.json.keys():
            setattr(job, key, request.json[key])

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
