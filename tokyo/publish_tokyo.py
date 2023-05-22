import time, json, ssl
from datetime import datetime
import paho.mqtt.client as mqtt

ENDPOINT = "a2jhw81yxp2s6o-ats.iot.ap-northeast-1.amazonaws.com"
THING_NAME = 'cloudIoT_10_ultrasonic_tokyo'
CERTPATH =  "/home/pi/project/tokyo/8ac757ec401470e2bf0550acda4752e5771d0bb53ae6a0a1a1b2fd4d25c2c65b-certificate.pem.crt" # cert파일 경로
KEYPATH = "/home/pi/project/tokyo/8ac757ec401470e2bf0550acda4752e5771d0bb53ae6a0a1a1b2fd4d25c2c65b-private.pem.key" # key 파일 경로
CAROOTPATH = "/home/pi/project/tokyo/AmazonRootCA1.pem" # RootCaPem 파일 경로
TOPIC = 'userDetect' #주제


current_time = datetime.now().strftime("%H:%M:%S")

def on_connect(mqttc, obj, flags, rc):
  if rc == 0: # 연결 성공
    print('connected!!')

try: 
  mqtt_client = mqtt.Client(client_id=THING_NAME)
  mqtt_client.on_connect = on_connect
  mqtt_client.tls_set(CAROOTPATH, certfile= CERTPATH, keyfile=KEYPATH, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
  mqtt_client.connect(ENDPOINT, port=8883)
  mqtt_client.loop_start()
  
  i=0
  while True: 
    payload = json.dumps({"msg":'user Detect!! - cloudIoT 10Team '+current_time}) #메시지 포맷
    mqtt_client.publish('userDetect', payload, qos=1) #메시지 발행
    i=i+1 
    time.sleep(2)
    if i==1:
      break


except KeyboardInterrupt:
    pass
  
mqtt_client.disconnect()
print(end='\n')
