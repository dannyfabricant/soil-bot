import requests

def send_data(url, readings):

	try:
		r = requests.post(url, data=readings)
		
		# Response, status etc
		print(r.text, r.status_code)
	except Exception as e:
		print(e)