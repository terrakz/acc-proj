import docker, uuid, json
from os import listdir

client = docker.from_env()

def run(data):
	time = data.get('time', '')
	problem = data.get('problem',1)
	method = data.get('method', 'FD') 
	result = data.get('result', 0)
	key = data.get('id', '')
	token = key if key else str(uuid.uuid4())
	if key == '' and time == '':
		print('creating docker service:', problem, method)
	elif key != '' and time != '':
		resultFile = open('./results/' + token + '.txt', 'a+')
		json.dump(data, resultFile)
		resultFile.write('\r\n')
	return token
