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
def run_table():
    #print(os.getcwd())
    #os.chdir('BENCHOP')
    #print(os.getcwd())
    #return octave.feval('Problem1a', nout=2, verbose=True,timeout=36000)
    #octave = oct2py.Oct2Py()
    #return octave.feval('myfun', 1, 2, 3)
   # return octave.feval('Problem1a').tolist()
    #return 123
    return run_problem1a()

def run_problem1a():
    cwd = os.getcwd()
    print(cwd)
    os.chdir('BENCHOP')
    print(os.getcwd())
    octave = oct2py.Oct2Py()
    result = json.dumps(octave.feval('Problem1a').tolist())
    os.chdir(cwd)
    return result
  

#@app.route('/task_pronoun_count', methods=['GET'])
#def task_pronoun_count():
#    return jsonify(fun_pronoun_count())

if __name__ == '__main__':
    celery.start()
    #app.run(host='0.0.0.0', debug=True)

