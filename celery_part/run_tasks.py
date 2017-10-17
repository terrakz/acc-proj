import time
from .celery_app import * #run_table 

if __name__ == '__main__':
 #for _ in range(1):
      result = run_table.apply_async()
      while not result.ready():
        print('sleeping 1 sec')
        time.sleep(1)
 

      print (result.result)
