#!/usr/bin/env python

import random, math
import json, os
import requests
import time
import datetime


def zipCode():
	return random.randint(math.pow(10, 2), math.pow(10, 3))

def transactionId():
	return random.randint(math.pow(10,9), math.pow(10, 10))

def basket():
	size = max((int)(random.gauss(5, 3)),1)
	return [random.randint(0, 4) for i in range(0, size)]

def totalAmount(itemsInBasket, i):
	factor = 1 if i < 2000 else 10
	return itemsInBasket*max((int)(random.gauss(70, 30)),10)/factor

def jsonLine(i):
	basketItems = basket()
	return json.dumps({
		"transactionId": transactionId(),
		"basket": basketItems if random.randint(0, 10) > 1 else None,
		"zipCode": zipCode() if random.randint(0, 10) > 1 else None,
		"totalAmount": totalAmount(len(basketItems), i) if random.randint(0, 10) > 1 else None
		})

for i in range(1, 10000):
	print("Sending request...")
	headers = {'content-type': 'application/json'}
	payload = jsonLine(i)
	print(payload)
	r = requests.post("http://localhost:5000/predict", data=payload, headers=headers)
	print("Received answer: " + str(r.text))
	time.sleep(1)

