from flask import Flask, render_template, jsonify, request
import requests
from gpiozero import Device,  DistanceSensor
import time
from flask_cors import CORS
import subprocess
import os

# PYTHONPATH 환경 변수 설정
env = os.environ.copy()
env["PYTHONPATH"] = "/usr/local/lib/python3.9/dist-packages"  # 실제 모듈 위치

distance = 0.3 # 기본 값
def ultrasonic(distance):
	sonic = DistanceSensor(echo=14, trigger=4)
	sonic.threshold_distance = distance

	if(sonic.wait_for_in_range()):
		subprocess.run(['python','./tokyo/publish_tokyo.py'],env=env, check=True)
		return True
	else: return false


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


if __name__=='__main__':
	app.run(host='0.0.0.0')

