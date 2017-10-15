
from .celery_app import run_table
if __name__ == '__main__':
   for _ in xrange(1):
      run_table.delay()
