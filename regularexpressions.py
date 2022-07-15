import re


string = "{'filenames':['prasad.exe', 'srinitha.exe','sai.exe']}"
res = re.sub("\'filenames\'\:(\[(.*)\])", "", string)
##res = re.sub("\'filenames\'\:", "", string)
##res2 = re.sub("","",res)

print(res)
