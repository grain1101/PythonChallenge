# http://www.pythonchallenge.com/pc/def/map.html

puzzle = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
url = "map"
ret = ""
for s in puzzle:
	if s.isalpha():
		ret = ret + chr((ord(s) - ord('a') + 2) % 26 + ord('a'))
	else:
		ret = ret + s
print ret

