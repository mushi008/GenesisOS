import time
import os

print("""   
──────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████──────────██████─██████████████─██████████████─██████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████████─██░░░░░░░░░░██──██░░██─██░░██████████─██░░██████████─████░░████─██░░██████████─
─██░░██─────────██░░██─────────██░░██████░░██──██░░██─██░░██─────────██░░██───────────██░░██───██░░██─────────
─██░░██─────────██░░██████████─██░░██──██░░██──██░░██─██░░██████████─██░░██████████───██░░██───██░░██████████─
─██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██───██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████████─██░░██──██░░██──██░░██─██░░██████████─██████████░░██───██░░██───██████████░░██─
─██░░██──██░░██─██░░██─────────██░░██──██░░██████░░██─██░░██─────────────────██░░██───██░░██───────────██░░██─
─██░░██████░░██─██░░██████████─██░░██──██░░░░░░░░░░██─██░░██████████─██████████░░██─████░░████─██████████░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████████████─██████──────────██████─██████████████─██████████████─██████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

print("""
[s] Continue With Setup Of Your Genesis
[c] I have already done my setup.
""")
setup = input("[?]: ")
if setup == 's':
    name = input(str("Please Enter Your Profile Name To Be Displayed:"))
    pas = input(str("Please Enter Your Login Password:"))
    lines = [name]
    with open('GenesisOS/User/username.txt', 'w') as gg:
        gg.writelines(lines)

    lines2 = [pas]
    with open('GenesisOS/User/Password.txt', 'w') as gg:
        gg.writelines(lines2)
        print("setup complete : )")
        input("Press Enter To Exit Window: ")

if setup == 'c':
    login_pass = open('GenesisOS/User/Password.txt')
    login_name = open('GenesisOS/User/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Enter Your password " + l_n + ": "))
    if login == l_p:
        os.system("python Home.py")
        break
    else:
        print("Wrong Password")

setup = input("[?]: ")
if setup == 's':
    name = input(str("Please Enter Your Profile Name To Be Displayed:"))
    pas = input(str("Please Enter Your Login Password:"))
    lines = [name]
    with open('GenesisOS/User/username.txt', 'w') as gg:
        gg.writelines(lines)

    lines2 = [pas]
    with open('GenesisOS/User/Password.txt', 'w') as gg:
        gg.writelines(lines2)
        print("setup complete : )")
        input("Press Enter To Exit Window: ")

if setup == 'c':
    login_pass = open('GenesisOS/User/Password.txt')
    login_name = open('GenesisOS/User/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Enter Your password " + l_n + ": "))
    if login == l_p:
        os.system("python Home.py")
        break
    else:
        print("Wrong Password")

