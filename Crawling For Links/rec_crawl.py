###################### Recursive Crawl ######################
# def crawl(address):
# 	for link in getMoreLinks(address):
# 		if "iitg.ernet.in" in link:
# 			if "http://" in link or "https://" in link:
# 				if ".htm" in link.split("/")[-1] or ".php" in link.split("/")[-1] or ".html" in link.split("/")[-1] or "." not in link.split("/")[-1]:
# 					if not exists(link):
# 						print("Trying ... link ", link)
# 						crawl(link)

##### #####
##### #####
##### ##### Didn't Work because recursive limit exceeds in python
##### #####
##### #####

# crawl("http://intranet.iitg.ernet.in")
