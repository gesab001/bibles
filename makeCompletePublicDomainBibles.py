import zipfile,fnmatch,os
import json


f = open("completePublicDomainBibles.json", "r", encoding="utf8")
completeBibleJson = json.loads(f.read())
f.close()

f = open("bibles.json", "r", encoding="utf8")
updatedBibleJson = json.loads(f.read())
f.close()

f = open("bibles.json", "r", encoding="utf8")
allBibles = json.loads(f.read())
f.close() 

count = 0
for language in allBibles["items"]:
  #print(language)
  versions = allBibles["items"][language]
  #print(versions)
  for version in versions:
    if version not in completeBibleJson:
      count = count + 1
      print(str(count) + version)
      updatedBibleJson["items"][language].pop(version, None)
  if bool(updatedBibleJson["items"][language])==False:
     updatedBibleJson["items"].pop(language, None)  
with open("bibles_complete_public_domain.json", "w", encoding="utf8") as outfile:
    json.dump(updatedBibleJson, outfile, ensure_ascii=False, indent=4)
       



