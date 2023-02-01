import json
import os
import zipfile

import zipfile,fnmatch,os



pathtokjv = os.path.join(r"C:\Users\giova\Desktop\bible_study_galaxy_watch", "kjv.json")
fopen = open(pathtokjv,"r", encoding="utf8")
bible = json.loads(fopen.read())
fopen.close()
version = bible["version"]
bookList = {}
for number in version:
    bookName = version[number]["book_name"]
    #print (bookName + ": " + number)
    bookList[bookName.replace(" ", "-")] = number

 
path = os.path.join(r"C:/Users/giova/Desktop/workspaces_updater", "booksOfTheBibleInDifferentLanguages.json") 

f = open(path, "r", encoding="utf-8")
booksOfTheBibleInDifferentLanguages = json.loads(f.read())
f.close()

def getLocalizedBookTitleList(targetLanguage):
  targetLanguage = targetLanguage.lower()
  if targetLanguage=="fil":
    targetLanguage= "tl"
  result = {}
  for bookCode in booksOfTheBibleInDifferentLanguages:

     localizedbooklist = booksOfTheBibleInDifferentLanguages[bookCode]
     if targetLanguage=="en":
         if "Song" in bookCode:
             bookCode = "Song-of-Songs"
             result[bookCode] = bookCode
         else:
             result[bookCode] = bookCode         
     else:          
      for key in localizedbooklist:

        if key.startswith(targetLanguage):
           booktitle = localizedbooklist[key][0]
           #print(booktitle)
           if "Song" in bookCode:
             bookCode = "Song-of-Songs"
           result[bookCode] = booktitle
      
  print(result)         
  return result

def getLocalizedBooks(languageCode):

    #languagejsJson = getLanguageJsJson(appFolder, languageCode)   
    #pathToLanguageJson = os.path.join(appFolder, "locales", languageCode, "language.json" )
    localeBookList  = getLocalizedBookTitleList(languageCode)
    #languagejsJson["localeBooks"] = {}
    #languagejsJson["localeBooks"] = localeBookList
    #with open(pathToLanguageJson, "w", encoding="utf8") as outfile:
    #  json.dump(languagejsJson, outfile, ensure_ascii=False, indent=4)
    return  localeBookList
    
def getBookNumber(bookName):
  print(bookList) 
  bookNumber = bookList[bookName.replace(" ", "-")]
  return bookNumber

def getWord(version, bookNumber, _chapter, _verse):
  #print(version)
  print("getWord")
  print(bookNumber)
  book = version[str(bookNumber)]

  chapter = book["book"][_chapter]

  verses = chapter["chapter"]  

  word = verses[_verse]["verse"].replace("\n", " ").strip()
  return word  


def getLocalizedBook(booklist, book):
  bookkey = ""
  if "Song" in book:
    bookkey = "Song-of-Songs"
  else:
    bookkey = book.replace(" ", "-")
  return   booklist.get(bookkey)

  

  
def getOriginalBibleVerses():
  f = open("en/bible.json", "r", encoding="utf8")
  jsondata = json.loads(f.read())
  f.close()
  return jsondata
missingVerses = {}
def translateBible(bibleversion):
    #source_dir  = os.path.join(appFolder, "language.js")
    #destination_dir = os.path.join(appFolder, "locales", languageCode, "language.js" )
    #languagejsJson = getOriginalBibleVerses()   
    #items = languagejsJson["items"]
    #localeBooks = getLocalizedBooks(languageCode)
    #bibleversion = languagejsJson["bibleversion"]
    #translate notes
    pathtobible = os.path.join(r"C:\Users\giova\Documents\bibles", bibleversion+".zip")
    with zipfile.ZipFile(pathtobible) as myzip:
     pathtojsoninsidezip = bibleversion + "/" + bibleversion + ".json"
     with myzip.open(pathtojsoninsidezip) as myfile:
        #print(myfile.read())
        bible = json.loads(myfile.read())
        versiontext = bible["version"]
        #print(versiontext) 
        missingVerses[bibleversion] = {"totalMissingVerses": 0}
        for bookNumber in versiontext:
          #print(bookNumber)
          bookName = versiontext[bookNumber]["book_name"]
          chapterJson = versiontext[bookNumber]["book"]
          #print(chapterJson)
          for chapterNumber in chapterJson:
            #print(chapterNumber)
            versesJson = chapterJson[chapterNumber]["chapter"]
            for verseNumber in versesJson:
               word = versesJson[verseNumber]["verse"]
               if word=="" or "bible version" in word or "translation" in word:
                 #print(bookName + " " + chapterNumber + ":" + verseNumber)
                 #print(word)
                 missingVerses[bibleversion]["totalMissingVerses"] = missingVerses[bibleversion]["totalMissingVerses"] + 1
        print(missingVerses)  
        print()        
    #pathToLanguageJson = os.path.join(languageCode, "bible.json" )

    #languagejsJson["localeBooks"] = localeBooks

    
def getBible(bibleversion):
    print("bibleversion: " + bibleversion)
    zipfile = bibleversion + ".zip"
    folder = bibleversion
    jsonfile = bibleversion + ".json"
    pathtozip = os.path.join(r"C:\Users\giova\Documents\bibles", zipfile )
    print("path: " + pathtozip)
    print(os.path.exists(pathtozip))
    #archive = zipfile.ZipFile(pathtozip, 'r')
    #jsondata = archive.read(folder + "/" + jsonfile)
    #print(jsondata)


rootPath = r"C:\Users\giova\Documents\bibles"
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):

        source = os.path.join(root, filename)
        
        print("source: " + source)
        #zipfile.ZipFile(source).extractall(os.path.join(root, "bible_folders"))
        bibleversion = os.path.splitext(filename)[0]
        #folder = code
        #print("folder: "  + folder)
        print("bibleversion: "  + bibleversion)

        translateBible(bibleversion)
        
        
with open("missingVerses.json", "w", encoding="utf8") as outfile:
      json.dump(missingVerses, outfile, ensure_ascii=False, indent=4)
  