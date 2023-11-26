files = ["plik1.txt",
         "plik2.txt",
         "plik3.txt"]
texty = ["text1", "text2", "text3"]

for filex, text in zip(files, texty):
    file = open(f"../files/{filex}", "w")
    file.write(text)
    file.close()
