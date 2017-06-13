
# def crawl(address):
# 	for link in getMoreLinks(address):
# 		if "iitg.ernet.in" in link:
# 			if "http://" in link or "https://" in link:
# 				if ".htm" in link.split("/")[-1] or ".php" in link.split("/")[-1] or ".html" in link.split("/")[-1] or "." not in link.split("/")[-1]:
# 					if not exists(link):
# 						print("Trying ... link ", link)
# 						crawl(link)


#
# crawl("http://intranet.iitg.ernet.in")
# http://intranet.iitg.ernet.in
# c.execute("DELETE FROM "+tableName)
# conn.commit()
#

# c.execute('CREATE TABLE IF NOT EXISTS '+tableName+'(address TEXT)')
# c.execute('DROP TABLE '+tableName+'')