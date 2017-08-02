# Pie
An Intranet Search Engine (Ongoing Project)

## Crawling The Intranet

```python
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

```

Crawling of intranet was done with the help of 'requests' library for Python 3. Beautiful Soup was used for the parsing of HTML for searching new links on visited pages.

```python
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
```
A database was implemented with Sqlite3 in the form of a stack. A database was required because the number of intranet links easily crossed 50,000 due to which it wasn't safe to implement it in a simple array or stack on RAM. 

When the database creation was complete, it needed some filtering as there were some duplicate links due to white spaces and other issues.
The code for filtering the links are present in the 'Cleaning' folder.

The links were then sorted and separated based on the domain names which were as shown in the image given below.
![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/3.png)

## Url Indexing

The indexing 
```python
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
```
