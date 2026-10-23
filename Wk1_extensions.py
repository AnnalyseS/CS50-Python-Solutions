ext = input("File name: ")

if ext.endswith(".gif"):
    print("image/gif")
elif ext.endswith(".jpg"):
    print("image/jpg")
elif ext.endswith(".jpeg"):
    print("image/jpeg")
elif ext.endswith(".png"):
    print("image/png")
elif ext.endswith(".txt"):
    print("image/txt")
elif ext.endswith(".pdf"):
    print("image/pdf")
elif ext.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")
    