q = input()
if q == "регистрация":
    log1 = input()
    pas1 = int(input())
    f = open("file.txt", 'w')
    f.write(log1)
    f.write(pas1)
    f.close()
if q == "авторизация":
    f = open("file.txt", 'r')
    text1 = f.readline
    text2 = f.readline
    if text1 == "" and text2 == "":
        print("сначала вы должны зарегестрироваться")
    elif:
        log2 = input()
        pas2 = int(input())
        if log2 == text1 and pas2 == text2:
            print("логин и пароль верны")
        else:
            print("пароль неверный")
    