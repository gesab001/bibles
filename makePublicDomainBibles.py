import zipfile,fnmatch,os
import json


f = open("completeBible.json", "r", encoding="utf8")
completeBibleJson = json.loads(f.read())
f.close()

f = open("completeBible.json", "r", encoding="utf8")
updatedBibleJson = json.loads(f.read())
f.close()

f = open("freebibles.json", "r", encoding="utf8")
freebibles = json.loads(f.read())
f.close() 

completeAndPublicDomainBibles = []
freeBiblesList = []
for x in range(0, len( freebibles)):
  item = freebibles[x]
  if "bibleversion" in item:
    bibleversion = item["bibleversion"]
    freeBiblesList.append(bibleversion)

print(freeBiblesList)  

for x in range(0,len( completeBibleJson)):
  bible = completeBibleJson[x]
  print(bible)  
  if bible in freeBiblesList:
    completeAndPublicDomainBibles.append(bible)
    
with open("publicDomainBibles.json", "w", encoding="utf8") as outfile:
    json.dump(completeAndPublicDomainBibles, outfile, ensure_ascii=False, indent=4)
       



