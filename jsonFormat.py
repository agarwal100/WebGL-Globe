import json


cityList = []
outstr = ""
for line in open('/Users/family/Downloads/pythonInput.txt','r'):
	cityList.append(json.loads(line))

for cityInfo in cityList[0:10]:


	outstr += str(cityInfo[" id"]) + ","

outstr = outstr[:-1]
textFile = open("Output.txt", "w")
textFile.write(outstr)
textFile.close()


print "finished"