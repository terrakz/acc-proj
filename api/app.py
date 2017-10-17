#!flask/bin/python
from flask import Flask, jsonify, request, send_from_directory, render_template, redirect, url_for, make_response
import sys, time, json, os
import dockerMethods

app = Flask(__name__, static_folder='static')

@app.route("/api/v1/result", methods=["GET"])
def index():
	#result = tasks.getEmAll.delay()
	#result.wait()
	result = request.args.get('id', 'John doe')
	return jsonify(result)#str(tasks.getEmAll())#jsonify(make_response(result))
#	return render_template('index.html', celery=result)

@app.route("/api/v1/result", methods=["POST"])
def create():
	#problem = request.args.get('problem', 1)
	#method = request.args.get('method', 'FD')
	id = dockerMethods.run(request.args)
	return id

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
#    port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0', port=port, debug=True)

