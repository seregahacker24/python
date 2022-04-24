z = 0
f = open("file.txt", 'r')
text1 = int(f.readline())
z = z + text1
text2 = int(f.readline())
z = z + text2
print(z)
f.close()