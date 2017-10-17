
from .celery_app import * #run_table 
if __name__ == '__main__':
 #for _ in range(1):
      x = run_table.delay()
      print(12345)
      print(x)
