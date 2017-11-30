from django.shortcuts import render
from HumanSensing import subscribe
import threading
import time

topic = "null"
payload = "null"
def conn():
	global topic, payload
	# topics = ['#']
	topics = ['uvafourier']
	m = subscribe.simple(topics, hostname="iot.eclipse.org", retained=False, msg_count=4)
	print("iteration", str(m[0].payload))
	for a in m:
		topic = a.topic
		payload = str(a.payload).split(",")[0][2]
	# payload = "1"
			
def index(request):
	MQTT_thread = threading.Thread(target=conn())
	MQTT_thread.start()

	element = {
		'topic': topic,
		'payload': payload
	}

	return render(request, 'index.html', element)
	# time.sleep(10)


def test(request):
	return render(request, 'index.html')