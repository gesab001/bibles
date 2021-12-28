import os


def getFileSize(zip_filename):
    file_size = os.path.getsize(zip_filename)
    print("File Size is :", file_size, "bytes")
    return file_size

files = os.listdir()
zipfiles = []
for f in files:
  if f.endswith(".zip"):
    zipfiles.append(f)
    getFileSize(f)
print(zipfiles)
    

