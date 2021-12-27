import json

filename = input("bible filename: " )
translationName = input("translation name: ")
f = open(filename, "r")

jsondata = json.loads(f.read())
books = jsondata["version"]
result = {}
for bookNumber in books:
    result["version"] = translationName
    bookname = books[bookNumber]["book_name"]
    result["book_name"] = bookname
    result["book_nr"] = bookNumber
    result["book"] = books[bookNumber]["book"]
    filename = bookname.replace(" ", "_") + ".json"
    with open("./"+translationName+"/"+filename, "w") as outfile:
       json.dump(result, outfile, indent=4)
    result = {"version": {} }   