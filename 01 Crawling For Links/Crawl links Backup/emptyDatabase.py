import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

conn = sqlite3.connect('links.db')
c = conn.cursor()

def add(link, tableName):
	c.execute('INSERT INTO '+tableName+' VALUES(?)',(link,))
	conn.commit()

def delete(link, tableName):
	c.execute('DELETE FROM '+tableName+' WHERE address == ?',(link,))
	conn.commit()

def delete_all(tableName):
	c.execute('DELETE FROM '+tableName)
	conn.commit()

def exists(link, tableName):
	c.execute('SELECT * FROM '+tableName+' WHERE address == ?',(link,))
	return False if len(c.fetchall()) == 0 else True

def find(link, tableName):
	c.execute('SELECT * FROM '+tableName+' WHERE address == ?',(link,))
	return c.fetchall()

def empty(tableName):
	c.execute('SELECT * FROM '+tableName)
	return True if len(c.fetchall()) == 0 else False

def insert(link, tableName):
	if not exists(link, tableName):
		add(link, tableName)
		return True
	else:
		return False

def pop(tableName):
	c.execute('SELECT * FROM '+tableName+' LIMIT 1')
	recv = c.fetchall()
	if len(recv) > 0:
		delete(recv[0][0], tableName)
		return recv[0][0]
	else:
		return None

def getMoreLinks(address):
	flag = False
	if "iitg.ernet.in" in address and ("http://" in address or "https://" in address) and len(address.split('/'))>=4 and not "eventcal" in address: # checking if legit intranet site
		name = address.split("/")[-1]
		if ".htm" in name or ".php" in name or ".html" in name or "." not in name: # checking if it is a html or php file or not
			if not exists(address, "visited"): # then if not already visited go ahead
				try:
					print(address, end=" - ")

					response = requests.get(address)
					soup = BeautifulSoup(response.text, "html.parser")

					insert(address,"visited")
					print("Crawled")

					morelinks = []
					for link in soup.find_all('a'):
						if link.get("href") != None:
							if not link.get("href").startswith("http"):
								morelinks.append(urljoin(address, link.get("href")))
							else:
								morelinks.append(link.get("href"))

					flag = True
					return morelinks
				except requests.exceptions.RequestException as e: 
			   		print(e)
	if flag == False:
		return []

#
# delete_all("stack")
# delete_all("visited")

#
# insert("http://intranet.iitg.ernet.in/","stack")
toCrawl = pop("stack")
while toCrawl!= None:
	for x in getMoreLinks(toCrawl):
		insert(x, "stack")
	toCrawl = pop("stack")

#
c.close()
conn.close()
