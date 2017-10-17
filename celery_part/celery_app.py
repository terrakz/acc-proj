import os
import oct2py

#import json

#from flask import Flask, jsonify
from celery import Celery


#app = Flask(__name__)
#app.config['CELERY_BROKER_URL'] = 'amqp://acc5:acc12345@localhost/acc5_vhost'
#app.config['CELERY_RESULT_BACKEND'] = 'amqp://acc5:acc12345@localhost/acc5_vhost'
celery = Celery('celery_part.celery', #app.name, 
                broker= 'amqp://acc5:acc12345@130.239.81.83:5672/acc5_vhost', #app.config['CELERY_BROKER_URL'], 
                backend='rpc://acc5:acc12345@130.239.81.83:5672/acc5_vhost') #app.config['CELERY_RESULT_BACKEND'])

@celery.task(bind=True)
def run_table(self):
    oc = oct2py.Oct2Py()
    return 123

#@app.route('/task_pronoun_count', methods=['GET'])
#def task_pronoun_count():
#    return jsonify(fun_pronoun_count())

if __name__ == '__main__':
    celery.start()
    #app.run(host='0.0.0.0', debug=True)

