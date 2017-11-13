from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from HumanSensing import subscribe



def index(request):
	# return HttpResponse("Hello, world. You're at Dr. Fourier's project index.")

	topics = ['uvafourier']


	topic = "yo"
	payload = "hmmm"

	"""
	while(1):
		m = subscribe.simple(topics, hostname="iot.eclipse.org", retained=False, msg_count=4)
		for a in m:
			print("Topic: " + (a.topic))
			print("Payload: " + str(a.payload))
	"""
	# 
	# m = subscribe.simple(topics, hostname="iot.eclipse.org", retained=False, msg_count=4)
	# 
	# for a in m:
	# 	topic = a.topic
	# 	payload = a.payload.split(",")[0]
	# 

	
	element = {
		'topic' : topic,
		'payload' : payload
	}

	#return render(request, 'index.html')
	return render(request, 'index.html', element)

def test(request):
	return render(request, 'index.html')