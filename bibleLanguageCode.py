import json

while True:
 fopen = open("bibleLanguageCode.json", "r")
 jsondata = json.loads(fopen.read())
 fopen.close()
 print(jsondata)


 bibleversion = input("bibleversion: " )
 langInput = input("languageCode: " )
 jsondata["VERSIONLANGUAGE"][bibleversion] = langInput

 with open("bibleLanguageCode.json", "w") as outfile:
  json.dump(jsondata, outfile, indent=4, sort_keys=True)