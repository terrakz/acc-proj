from pprint import pprint
import sys
import json
import re
import os

pronouns = {'han' : 0, 'hon' : 0, 'den' : 0, 'det' : 0, 'denna' : 0, 'denne' : 0, 'hen' : 0}

def iterateAllFiles():
	for file in os.listdir('./data'):
		oneFile(file)
	return pronouns

def findEmAll():
	regex = re.compile('[^a-zA-Z ]')
	for filename in os.listdir('./data'):
		with open('./data/' + filename, 'rw') as file:
			for line in file:
				if line[0] == '{':#not line.isspace() and line[0] is '{':
					jsonTweet = json.loads(line)
					if jsonTweet.get('retweeted_status') != None:
						words = regex.sub(' ', jsonTweet.get('text', '').lower()).split()
						for word in words:
							if word in pronouns:
								pronouns[word] += 1
	return pronouns

def oneFile(filename):
	fileobj = open('./data/' + filename)
	lineread(filename)

def testOne():
	oneFile('0ecdf8e0-bc1a-4fb3-a015-9b8dc563a92f')
	return pronouns

def processPronouns(tweettxt):
	for key, value in pronouns.iteritems():
		if key in tweettxt:
			pronouns[key] = value + 1


def lineread(filepath):
	fileobj = open('./data/'+filepath)
	try:
		lines = fileobj.readlines()
		for line in lines:
			if not line.isspace() and line[0] is '{':
				jtweet = json.loads(line)
				tweettxt = jtweet['text'].lower().split()
				processPronouns(tweettxt)
	finally:
		fileobj.close()

