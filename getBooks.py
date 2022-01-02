import json
import os
import subprocess
import zipfile
from os.path import basename
import shutil

filename = input("bible filename: " )
language = input("language: " )
translationName = input("abbreviation bible name: ")
fullName = input("full name: ")
f = open(filename, "r")

jsondata = json.loads(f.read())
f.close()

books = jsondata["version"]
result = {}

def updateBiblesList(language, translation, totalSize):
    f = open("bibles.json", "r")
    biblelistjson = json.loads(f.read())
    if language in biblelistjson["items"].keys():
        print("Key exists")   
        biblelistjson["items"][language][translation] = {"totalSize": 0}        
    else:
        print("Key does not exist")
        biblelistjson["items"][language] = {}
        biblelistjson["items"][language] = {translation: {"fullName": "", "totalSize": 0}}
    biblelistjson["items"][language][translation]["totalSize"] = totalSize
    biblelistjson["items"][language][translation]["fullName"] = fullName
    print(biblelistjson)
    with open("bibles.json", "w") as outfile:
      json.dump(biblelistjson, outfile, indent=4, sort_keys=True)
    
def getFileSize(zip_filename):
    file_size = os.path.getsize(zip_filename)
    print("File Size is :", file_size, "bytes")
    return file_size
    
def zipBooks(folder):
    # create a ZipFile object
    isExist = os.path.exists(folder+'.zip')
    if isExist:
      print(folder + ".zip" + " already exists. try a different filename")
    else:  
     with zipfile.ZipFile(folder+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipObj:

       for folderName, subfolders, filenames in os.walk(folder):
           for filename in filenames:
               #create complete filepath of file in directory
               filePath = os.path.join(folderName, filename)
               # Add file to zip
               zipObj.write(filePath, filePath) 
  

for bookNumber in books:
    result["version"] = translationName
    bookname = books[bookNumber]["book_name"]
    result["book_name"] = bookname
    result["book_nr"] = bookNumber
    result["book"] = books[bookNumber]["book"]
    book_filename_json = bookname.replace(" ", "_") + ".json"
    path = "./"+translationName+"/"+book_filename_json
    isExist = os.path.exists(translationName)
    print(isExist)
    if not isExist:
      os.makedirs(translationName)
    with open(path, "w") as outfile:
       json.dump(result, outfile, indent=4)
    result = {"version": {} }   


os.rename(filename, translationName+".json")
# absolute path
src_path = translationName+".json"
dst_path = "./"+translationName + "/" +  translationName+".json"
shutil.move(src_path, dst_path )    
zipBooks(translationName)  
updateBiblesList(language, translationName, getFileSize(translationName+".zip"))
shutil.rmtree(translationName)