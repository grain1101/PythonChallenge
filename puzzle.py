import requests


s = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'
num = 16044/2
while True:
	r = requests.get(s % (num))
	print r.text
	#if r.text.split()[-1] == 
	num = int(r.text.split()[-1])