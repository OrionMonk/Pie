First, the links are separated into the different domains namely: auto, automation, bidya, csea, eict, iitg, intranet, jatinga, kamrup, kolong, local, loktak, nptel, phones, shilloi, webmail and www.iitg and store them in the "separated" folder.

Then, we create a word index for each of the URLs in the files of the "separated" folder based on valid keywords using the 'PyEnchant' dictionary with the mergeIndexes.py program and then save it into json files.

Finally, we merge all the json indices into one big json file named "merge_<num of word indices>.json"

