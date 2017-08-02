# Pie
An Intranet Search Engine (Ongoing Project)

## Crawling The Intranet
The web crawling process was initiated with the official home page of the intranet. All the links obtained were then filtered for unique valid links in this part of the process.

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

Crawling of intranet was done with the help of **requests** library for Python3. We used **Beautiful Soup** for the parsing of HTML for searching new links on visited pages.

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
A database was implemented with **Sqlite3** as a stack. A database was required because the number of intranet links to be crawled easily crossed 50,000 due to which it wasn't safe to implement it in a simple array or stack on RAM. 

When the database creation was complete, it needed some filtering as there were some duplicate links due to white spaces and other issues.
The code for filtering the links are present in the 'Cleaning' folder.

The links were then sorted and separately stored based on the domain names which are as shown in the image given below.
![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/sub-domains.png)

## Url Indexing

The second part of the process was to index the webpages based on the url of each link. An english *spell-check* library called **PyEnchant** was used for preprocessing valid words for url indexing. Here, lexes are used to mean the indexed keywords.
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
			
	.
	.
	.
	
for link in links:
	fk_string = link.split("//")[1].strip().strip(" ").strip("/").split("/")

	for f_string in fk_string:
		for string in re.split(r'[0-9\-\?\=&\.\(\)\+\_]',f_string):
			i = 0
			
			while i < len(string):
				for j in range(len(string)-1, i+1, -1):
				
					if isWord.check(string[i:j+1]):
						add_key(lexes,string[i:j+1], link.strip())
					elif string[i:j+1].lower() in tags:
						add_key(lexes,string[i:j+1], link.strip())
```

The indexes were then stored in Json format separately for the various sub-domains. 

```python
# for each filename (which here mean the separate sub domains which are stored in separate files)
with open(filename.split('/')[1].split(".txt")[0]+'.json', 'w') as fp:
	json.dump(lexes, fp, sort_keys=True, indent=4)
```

The indexes were then finally merged into a huge file of 6,581 keywords.The Json Output File looks like:
![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/url-indice.png)
