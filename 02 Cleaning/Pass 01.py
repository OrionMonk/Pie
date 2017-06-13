import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

############################## Connecting to SQLite Database ######################################
conn = sqlite3.connect('links.db')
c = conn.cursor()

############################## SQL Queries ####################################

def all():
	c.execute('SELECT * FROM visited ORDER BY ?', ("address",))
	tmp = []
	for x in c.fetchall():
		tmp.append(x[0])
	return tmp

validLinks = sorted(all(),key = lambda x: x.split("//")[1])
i = 0
print(len(validLinks))
with open("intranetlinks.txt","w") as file:
	for x in validLinks:
		if len(x.split("http://")) == 2 or len(x.split("https://")) == 2:
			try:
				file.write("http"+x.split("http")[-1]+"\n")
				i += 1
			except:
				print(validLinks[i])