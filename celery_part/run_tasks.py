import time
from celery import group
from .celery_app import *

if __name__ == '__main__':
     #result = run_table.apply_async()
     #while not result.ready():
     #  print('sleeping 1 sec')
     #  time.sleep(1)
 
     # print (result.result)

     result = group(run_problem.s(i) for i in range(1,10))()
     result.get(36000)
