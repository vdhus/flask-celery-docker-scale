import os
from flask import Flask, jsonify, request
from flask import url_for
from worker import celery
from celery.result import AsyncResult
import celery.states as states

env = os.environ
app = Flask(__name__)


@app.route('/calc', methods=['POST'])
def calc():
    data = request.json['data']
    task = celery.send_task('mytasks.calc', args=[data], kwargs={})
    res = celery.AsyncResult(task.id)
    return jsonify({
            'id': task.id,
            'status': res.state,
            'url': url_for('check_task', id=task.id,_external=True)
        })


@app.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    if res.state==states.PENDING:
        return jsonify({
            'status': res.state,
            'data': None,
        })
    else:
        return jsonify({
            'status': 'FINISHED',
            'data': res.result,
        })

if __name__ == '__main__':
    app.run(debug=env.get('DEBUG',True),
            port=int(env.get('PORT',5000)),
            host=env.get('HOST','0.0.0.0')
    )
