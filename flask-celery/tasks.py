import os
import time
from celery import Celery

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


# @TODO: replace this method with the actual optimization:
def find_optimal_bids(data):
	time.sleep(10)
	return {
		'optimal_bids': '@todo: calculate optimal bids',
	}


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.calc')
def calc(data):
	result = find_optimal_bids(data)
	return result
