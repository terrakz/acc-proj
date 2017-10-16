#from oct2py import octave
from oct2py import Oct2Py, get_log
import numpy as np
import json, requests, time, sys

#octave.addpath('/home/ubuntu/acc-proj/BENCHOP/')
#octave.eval('quicktable()')
#octave.quicktable()
#octave.feval('/home/ubuntu/acc-proj/BENCHOP/quicktable.m')
#oc = Oct2Py(logger=get_log())
#oc.logger = (get_log('new_log')
#oc.logger.setLevel(logging.INFO)
#octave.feval('/home/ubuntu/acc-proj/BENCHOP/add.m', 1, 2)
#Oct2Py.feval('/home/ubuntu/acc-proj/BENCHOP/add.m', 1, 2)
def run(problem, method):
	oc = Oct2Py()
	x = oc.add(2, 2)
	return x


if __name__ =="__main__":
	start = time.time()
	print(sys.argv)
	print(len(sys.argv))
	if(len(sys.argv) == 4):
		problem = sys.argv[1] if sys.argv[1] else 'none'
		method = sys.argv[2] if sys.argv[2] else 'none'
		api = sys.argv[3] if sys.argv[3] else '0.0.0.0'
		api = 'http://' + api + ':5000/api/v1/result'
		result = run(problem, method)
		result = run(problem, method)
		finished = time.time()
		resultTime = finished - start
		print('running problem: ' + problem + ' method: ' + method + ' result: ' + str(result) + ' time: ' + str(resultTime) + ' target api: ' + api)
		try:
			r = requests.post(api, data={'problem': problem, 'method': method, 'time': resultTime, 'result': result})
		except requests.exceptions.RequestException as e:
			print e
			sys.exit(1)
		print(r.status_code, r.reason)
	else:
		print('come on pass me 3 arguments! (problem, method, apiIP)')
