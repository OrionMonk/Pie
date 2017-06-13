with open("links 01.txt","r") as file:
	arr = file.readlines()
pages = []
piles = set()
for x in arr:
	page = x.split("#")[0]
	if page not in piles:
		pages.append(page)
		piles.add(page)

with open("links 02.txt","w") as file:
	for x in pages:
		file.write(x.split("\n")[0]+"\n")

print(len(pages))