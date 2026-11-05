#final working code
from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Input Username: ")
    password = getpass("Input password: ")

    if username == "Ana" and password == "haduken12":
        print("Access granted")
        isLogin = True
    else:
        print("access denied")
        isLogin = False

