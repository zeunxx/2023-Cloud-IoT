from flask import Flask, render_template, jsonify, request
import requests
from gpiozero import DistanceSensor
import time
from flask_cors import CORS
import subprocess


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


distance = 0.3 # 기본 값
def ultrasonic(distance):
	sonic = DistanceSensor(echo=14, trigger=4)
	sonic.threshold_distance = distance

	if(sonic.wait_for_in_range()):
		subprocess.run(['python','./tokyo/publish_tokyo.py'], check=True)
		return userIn(sonic)
	else:
		print("그외")
		return userOut(sonic)

def userIn(sonic):
	print("in ", sonic.distance*100," cm")
	return True
def userOut(sonic):
	print("out ", sonic.distance*100," cm")
	return False

app.route("/")
def home():
	return 'ok'

@app.route("/move")
def sonic():
	global distance

	move = ultrasonic(distance)
	print(move)
	if move:
		data = {'result':'user In'}
		return  jsonify(data)
	else:
		data = {'result':'user Out'}
		return jsonify(data)

@app.route("/set_distance")
def set_distance():
	global distance
	arg = request.args.get('value')
	if arg!=None:
		distance = float(arg)
	print(distance)
	return str(distance)

@app.route("/test")
def test():
	return "flask ok"

if __name__=='__main__':
	app.run(host='0.0.0.0')

