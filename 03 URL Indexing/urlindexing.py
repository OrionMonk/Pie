import requests
from bs4 import BeautifulSoup
import os
import enchant
import json
import re

tags = ["btech","mtech","b.tech","m.tech","phd","cse","mnc","eee","des","bdes","mdes","vlsi","sem"]

def add_key(lexes, string, link):
	string = string.lstrip()
	if string != "":
		if string in lexes:
			if link.strip() not in lexes[string]:
				lexes[string] += [link.strip()]
		else:
			lexes[string] = [link.strip()]

dir = "Separated/"
files = os.listdir(dir)
for file in files:
	print(file)
	filename = dir+file

	isWord = enchant.Dict("en_US")

	with open(filename,"r") as file:
		links = file.readlines()

	print(len(links))
	lexes = {}
	for link in links:
		# print(link)
		fk_string = link.split("//")[1].strip().strip(" ").strip("/").split(".html")[0].split(".htm")[0].split(".php")[0].split("/")

		for f_string in fk_string:
			add_key(lexes,f_string, link.strip())
			for string in re.split(r'[0-9\-\?\=&\.\(\)\+\_]',f_string):
				if string != "":
					k = -1
					i = 0
					# print(string)
					while i < len(string):
						flag = False
						for j in range(len(string)-1, i+1, -1):
							# print(string[i:j+1])

							if isWord.check(string[i:j+1]):
								add_key(lexes,string[i:j+1], link.strip())

								if k != -1:
									if i-k > 1:
										add_key(lexes,string[k:i], link.strip())
									k = -1
								if string[j] != 's':
									i = j+1
									flag = True
									break
						if i == len(string)-1:
							if k != -1:
								if i-k > 1:
									add_key(lexes,string[k:i+1],link.strip())
								k = -1
						if not flag:
							if k == -1:
								k = i
							i += 1
	print("pass1")
	for link in links:
		# print(link)
		fk_string = link.split("//")[1].strip().strip(" ").strip("/").split("/")

		for f_string in fk_string:
			for string in re.split(r'[0-9\-\?\=&\.\(\)\+\_]',f_string):
				i = 0
				while i < len(string):
					for j in range(len(string)-1, i+1, -1):
						# print(string[i:j+1])
# 
						if isWord.check(string[i:j+1]):
							add_key(lexes,string[i:j+1], link.strip())
						elif string[i:j+1].lower() in tags:
							add_key(lexes,string[i:j+1], link.strip())

					i += 1
	print("pass2")

	# for x in lexes:
	# 	print(x)
	# print(lexes)
	with open(filename.split('/')[1].split(".txt")[0]+'.json', 'w') as fp:
	    json.dump(lexes, fp, sort_keys=True, indent=4)