import os
import oct2py
import numpy as np
import json

#from flask import Flask, jsonify
from celery import Celery


#app = Flask(__name__)
#app.config['CELERY_BROKER_URL'] = 'amqp://acc5:acc12345@localhost/acc5_vhost'
#app.config['CELERY_RESULT_BACKEND'] = 'amqp://acc5:acc12345@localhost/acc5_vhost'
celery = Celery('celery_part.celery', #app.name, 
                broker= 'amqp://acc5:acc12345@130.239.81.83:5672/acc5_vhost', #app.config['CELERY_BROKER_URL'], 
                backend='rpc://acc5:acc12345@130.239.81.83:5672/acc5_vhost') #app.config['CELERY_RESULT_BACKEND'])

@celery.task()
def run_problem(index):
    cwd = os.getcwd()
    print(cwd)
    os.chdir('BENCHOP')
    print(os.getcwd())
    octave = oct2py.Oct2Py()
    result = None
    if index == 1:
       result = json.dumps(octave.feval('ProblemI1a').tolist())
    elif index == 2:
       result = json.dumps(octave.feval('ProblemI1b').tolist())
    elif index == 3:
       result = json.dumps(octave.feval('ProblemI1c').tolist())
    elif index == 4:
       result = json.dumps(octave.feval('ProblemII1a').tolist())
    elif index == 5:
       result = json.dumps(octave.feval('ProblemII1b').tolist())
    elif index == 6:
       result = json.dumps(octave.feval('ProblemII1c').tolist())
    else:
       None
    os.chdir(cwd)
    return result


#@app.route('/task_pronoun_count', methods=['GET'])
#def task_pronoun_count():
#    return jsonify(fun_pronoun_count())

if __name__ == '__main__':
    celery.start()
    #app.run(host='0.0.0.0', debug=True)

