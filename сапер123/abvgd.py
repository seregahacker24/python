import mylib
import random
qw = 0
def mina():
    for q in range(3):
        a = random.randint(0, 11)
        b = random.randint(0, 11)
        mylib.pole[a][b] = "@"
def minacheck():
    if mylib.pole[stroka - 1][stolb - 1] == "@":
        print("Ты попал на мину и проиграл")
        mylib.vyvodPolya(mylib.pole)
        game = False
def mina123(stroka,stolb):
    if mylib.vidimost_polya[stroka][stolb] == "•":
        mylib.vidimost_polya[stroka][stolb] = mylib.pole[stroka][stolb]
        if mylib.pole[stroka][stolb] == "*":
            if stroka-1 >= 0:
                if mylib.pole[stroka-1][stolb] == "@":
                    qw = qw + 1   
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    if mylib.pole[stroka-1][stolb-1] == "@":
                        qw = qw + 1
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    if mylib.pole[stroka-1][stolb+1] == "@":
                        qw = qw + 1
                    check(stroka-1,stolb+1)
            if stroka+1 < len(pole):
                if mylib.pole[stroka+1][stolb] == "@":
                    qw = qw + 1
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    if mylib.pole[stroka+1][stolb-1] == "@":
                        qw = qw + 1
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    if mylib.pole[stroka+1][stolb+1] == "@":
                        qw = qw + 1
                    check(stroka+1,stolb+1)
            if stolb-1 >= 0:
                if mylib.pole[stroka][stolb-1] == "@":
                    qw = qw + 1
                check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                if mylib.pole[stroka][stolb+1] == "@":
                    qw = qw + 1
                check(stroka,stolb+1)
            mylib.vidimost_polya[stroka][stolb] = qw
mina()
mylib.vyvodPolya(mylib.vidimost_polya) ##############################
game = True
while game:
    stroka = int(input())
    stolb = int(input())
    if stroka > 12:
        stroka = 12
    if stroka < 1:
        stroka = 1
    if stolb > 12:
        stolb = 12
    if stolb < 1:
        stolb = 1
    minacheck()
    mylib.check(stroka-1,stolb-1)
    mina123(stroka,stolb)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False
print("Всё поле открыто и ты выиграл!")