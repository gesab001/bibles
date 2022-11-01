import json

f = open("UZB.json", "r", encoding="utf8")
jsondata = json.loads(f.read())["version"]
count = 1
string = ""
for key in jsondata:

  book_name = jsondata[key]["book_name"]
  chapters = jsondata[key]["book"]
  for c in chapters:
    verses = chapters[c]["chapter"]

    for v in verses:

      verse = verses[v]["verse"]
      if verse=="":
        reference = book_name + " " + c + ":"+v
        print(str(count)+ ". " + reference)
        print(verse)
        string = string + str(count)+ ". " + reference
        string = string + verse
        string = string + "\n\n"
        count = count + 1

print(string)        
with open("../notexist.txt", "w") as writer:
  writer.write(string)        