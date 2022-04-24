z = ""
f = open("file1.txt", 'r')
text1 = f.readline()
f.close()
f = open("file2.txt", 'r')
text2 = f.readline()
f.close()
z = text1 + text2
f = open("file1.txt", 'w')
f.write(z)
f.close()