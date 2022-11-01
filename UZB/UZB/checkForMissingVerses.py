import json

f = open("UZB.json", "r", encoding="utf8")
jsondata = json.loads(f.read())["version"]
for key in jsondata:

  book_name = jsondata[key]["book_name"]
  chapters = jsondata[key]["book"]
  for c in chapters:
    verses = chapters[c]["chapter"]

    for v in verses:

      verse = verses[v]["verse"]
      if verse=="":
        reference = book_name + " " + c + ":"+v
        print(reference)
        print(verse)