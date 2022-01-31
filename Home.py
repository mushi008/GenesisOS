import time
import os
import socket
import psutil

print("Desktop")
battery = psutil.sensors_battery()
login_pass = open('GenesisOS/User/Password.txt')
login_name = open('GenesisOS/User/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
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

print("Welcome " + l_n)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("The Time Is: " + time.strftime('%H:%M %p'))
print("Battery: ")
print(battery.percent)
print("""
[t] Open Text Editor
[b] Open Browser
[f] Open File Explorer
[s] Configure/Open BioS
[e] Exit
[m] Clock
""")
setup = input("[?]: ")
if setup == 't':
    os.system('python Text.py')

if setup == 'b':
    os.system('python browser.py')

if setup == 'f':
    os.system('explorer')

if setup == 'm':
    os.system('python Clock.py')

if setup == 's':
    while True:
        b_login = input(str("Please Enter Your Password " + l_n + " To Open Bios: "))
        if b_login == l_p:
            print("Opening Bios...")
            host_name = socket.gethostname()
            hos_ip = socket.gethostbyname(host_name)
            print("[u] USERNAME: " + l_n)
            print("[p] PASSWORD: " + l_p)
            print("HOST NAME: " + host_name)
            print("LOCAL IPS: " + hos_ip)
            edit_b = input("Enter [?] to change setting: ")
            if edit_b == 'p':
                edit_n = input("Enter New Username: ")
                with open('GenesisOS/User/username.txt', 'w') as gg:
                    gg.writelines(edit_n)
                print("Username changed to " + edit_n)
                input("Press e To Close Window: ")
                if setup == e:
                    quit()

            if edit_b == "s":
                edit_p = input("Enter New Password: ")
                with open('GenesisOS/User/Password.txt', 'w') as gg:
                    gg.writelines(edit_p)

                print("Password changed to " + edit_p)
                input("Press e to close window: ")
                if setup == e:
                    quit()



            else:
                print("Wrong Password To " + l_n)

if setup == 'e':
    input('Press ENTER to exit safely')
