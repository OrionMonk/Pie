import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


######################### Create Table ########################## Commented after table was created

# c.execute('CREATE TABLE IF NOT EXISTS '+tableName+'(address TEXT)')
# c.execute('DROP TABLE '+tableName+'')


############################## Connecting to SQLite Database ######################################
conn = sqlite3.connect('links.db')
c = conn.cursor()

############################## SQL Queries ####################################
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

################################ Get Links Functions ############################################

# Scrape a given page for further links within it using Beautiful Soup
def getMoreLinks(address):
	flag = False
	address = address.split("#")[0]
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

	# if no links found or address is invalid
	if flag == False:
		return []

############################ Main Code #################################

# Main Crawl Start site
insert("http://intranet.iitg.ernet.in/","stack") # Commented when once the site has been crawled

# initial pop of a link from the stack table of the database
toCrawl = pop("stack")
while toCrawl!= None:
	for x in getMoreLinks(toCrawl):
		insert(x, "stack") # inserting newly found links to the stack table in database

	toCrawl = pop("stack")

############################ Closing used database #######################
c.close()
conn.close()
