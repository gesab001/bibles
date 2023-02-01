import zipfile,fnmatch,os

rootPath = r"C:\Users\giova\Documents\bibles"
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):

        source = os.path.join(root, filename)
        #os.path.splitext(filename)[0])
        print("source: " + source)
        zipfile.ZipFile(source).extractall(os.path.join(root, "bible_folders"))