from oct2py import Oct2Py, get_log
import json, requests, time, sys

def run(problem, method):
	oc = Oct2Py()
	x = oc.qtable2(problem, method)
	# qtable2(1,'COS')
	return x


if __name__ =="__main__":
	start = time.time()
	print(sys.argv)
	print(len(sys.argv))
	if(len(sys.argv) == 4):
		problem = sys.argv[1]
		method = sys.argv[2]
		api = sys.argv[3]
		api = 'http://' + api + ':5000/api/v1/result'
		result = run(problem, method)
		finished = time.time()
		resultTime = finished - start
		print('running problem: ' + problem + ' method: ' + method + ' result: ' + str(result) + ' time: ' + str(resultTime) + ' target api: ' + api)
		try:
			#r = requests.post(api, data={'problem': problem, 'method': method, 'time': resultTime, 'result': result, 'id': '7b1d5f1d-d293-46c3-8883-f809344663ad'})
			r = requests.post(api, data={{"id": "7b1d5f1d-d293-46c3-8883-f809344663ad", "method": "COS", "problem": 999, "result": 999, "time": 999}})
		except requests.exceptions.RequestException as e:
			print (e)
			sys.exit(13379)
		print(r.status_code, r.reason)
	else:
		print('come on pass me 3 arguments! (problem, method, apiIP)')
