import json
import os

indexes = {}

files = os.listdir()
for file in files:
	if file.endswith(".json"):
		with open(file,"r") as fp:
			tmp = json.loads(fp.read())

		for key in tmp:
			if key not in indexes:
				indexes[key] = tmp[key]
			else:
				indexes[key] += tmp[key]

with open("merged_"+str(len(indexes))+".json","w") as fp:
	json.dump(indexes, fp, sort_keys=True, indent=4)