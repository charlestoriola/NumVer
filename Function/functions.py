from os import system
def next():
    if not input("Press ENTER to continue"):
        system("clear")
        return
    else:
        system("clear")
        next()


def verify(num):
    #Check whether the number entered is a Nigerian phone number

    try:
        check = [int(num[i]) for i in range(0 ,len(num))]
    except:
        print("Why you put in them other symbols dawg?")
    if len(num) == 11 or len(num) == 10 or (len(num) == 14 and "+234" in num):
        return True
    return False
