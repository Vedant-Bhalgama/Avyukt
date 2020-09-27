# Avyukt - Exploitation Framework (Version-Beta)

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Vedant-Bhalgama/Avyukt/issues)

Avyukt is a Exploitation Framework which can be used to generate Malicious Payloads and exploit Windows OS. It is completely written in `python2`. For now, I have only released a Beta Version. More updated features and better payloads are going to be added soon in the final version.<br>

    - Only made for Penetration Testing Purpose for White-Hat Hackers 
    - Use with caution.
    - You will be responsible for your actions. 
    - We assume no liability and are not responsible for any misuse or damage.
        
- Framework Version : 1.1.1 (Beta)
- Developed by : [Vedant-Bhalgama](https://github.com/Vedant-Bhalgama)
- Framework Testers : GOWTHAM-OFFICIAL-PGN

# Resources
- [Avyukt - Exploitation Framework (Version-Beta)](#avyukt---exploitation-framework-version-beta)
- [Resources](#resources)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
    - [From Source](#from-source)
    - [From Github](#from-github)
- [Running Avyukt](#running-avyukt)
- [Under Development](#under-development)
- [Have Suggestion](#have-suggestion)
- [Video Tutorial for Framework](#video-tutorial-for-framework)
- [Special Thanks To](#special-thanks-to)
- [Developed By](#developed-by)


# Features
 - Screenshot Ability
 - Upload Files
 - Download Files
 - Execute any System Command
 - Directory Navigation (cd command)
 - Persistent 

# Installation Instructions

### From Source

Download the zip file from the [release](https://github.com/Vedant-Bhalgama/Avyukt/releases/latest) page. Unzip it and change your working directory to Avyukt.

```sh
▶ cd Avyukt; pip install -r requirements.txt; python Avyukt_Setup/setup.py; 
```

### From Github

```sh
▶ git clone https://github.com/Vedant-Bhalgama/Avyukt; cd Avyukt; pip install -r requirements.txt; python Avyukt_Setup/setup.py; 
```

# Running Avyukt

To run the Avyukt Framework , just use the following command.
```sh
▶ python ./Avyukt.py
    _                    _    _     __  __
   / \__   ___   _ _   _| | _| |_  |  \/  | ___ _ __  _   _
  / _ \ \ / / | | | | | | |/ / __| | |\/| |/ _ \ '_ \| | | |
 / ___ \ V /| |_| | |_| |   <| |_  | |  | |  __/ | | | |_| |
/_/   \_\_/  \__, |\__,_|_|\_\\__| |_|  |_|\___|_| |_|\__,_|
             |___/


        Version 1.0 (Beta)

        ==============
        Core Commands
        ==============

                Commands        Description

                1) Evasion      A list of payloads to exploit target
                2) Listener     A list of handlers to recieve reverse connection
                3) Help         A list of commands and how to use them
                4) Exit         Exit the framework

        Menu Info

                Number of Listeners : 3
                Number of Payloads : 12
                Developed by : Vedant Bhalgama

Avyukt>:
```
**Evasion**
```sh
    _                    _    _     _____                _
   / \__   ___   _ _   _| | _| |_  | ____|_   ____ _ ___(_) ___  _ __
  / _ \ \ / / | | | | | | |/ / __| |  _| \ \ / / _` / __| |/ _ \| '_ \
 / ___ \ V /| |_| | |_| |   <| |_  | |___ \ V / (_| \__ \ | (_) | | | |
/_/   \_\_/  \__, |\__,_|_|\_\\__| |_____| \_/ \__,_|___/_|\___/|_| |_|
             |___/


[+] Select the payload you want to use, Only This Is available for now

                Avyukt Payloads for Windows (Excellent)

                [1] python/Avyukt/reverse_tcp (Highly Obfuscated exe)

                [2] python/Avyukt_NC/reverse_tcp

                [3] python/Avyukt/reverse_tcp (Non - Obfuscated exe)

                [4] python/Avyukt/reverse_tcp (Python File)

                Avyukt Payloads for Linux (Good)

                [5] python/Avyukt/reverse_tcp (Linux)

                MsfVenom Payloads (Poor)

                [6] windows/meterpreter/reverse_https

                [7] windows/meterpreter/reverse_tcp

                [8] windows/meterpreter/reverse_http

                Normal Python Payloads (Good)

                [9] python/meterpreter/reverse_https

                [10] python/meterpreter/reverse_tcp

                [11] python/meterpreter/reverse_http

                Android Backdoors (Good)

                [12] android/meterpreter/reverse_tcpz

        [+] Press Enter to return to Menu

Avyukt(Evasion)>:
```
**Listener**
```sh
    _                    _    _     _   _                 _ _
   / \__   ___   _ _   _| | _| |_  | | | | __ _ _ __   __| | | ___ _ __ ___
  / _ \ \ / / | | | | | | |/ / __| | |_| |/ _` | '_ \ / _` | |/ _ \ '__/ __|
 / ___ \ V /| |_| | |_| |   <| |_  |  _  | (_| | | | | (_| | |  __/ |  \__ \
/_/   \_\_/  \__, |\__,_|_|\_\\__| |_| |_|\__,_|_| |_|\__,_|_|\___|_|  |___/
             |___/


        [+] Handler Menu

                [1] Avyukt Handler (Works with python/Avyukt/reverse_tcp Payload in Evasion Menu)

                [2] msfconsole (Works only with meterpreter Payloads in Evasion Menu)

                [3] NetCat Listener (Works only with PowerShell Payload and avyukt_NC in Evasion Menu)

        [+] Press Enter to go back

Avyukt(Handlers)>:
```

# Under Development
  - More Undetectable Payloads going to be added
  - Webcam Snap (Take images of Target from their WebCam)
  - New Listener View

# Have Suggestion
Having Ideas for Framework? <br> Don't be shy! <br>Submit them here

https://docs.google.com/forms/d/1YKYxLAYj0R0P5TS3bnnPkdGVKZuiS6rrWCLgH_2Kzao

# Video Tutorial for Framework
[Youtube Link](https://www.youtube.com/watch?v=ecPv9EEsbnY)

# Special Thanks To
    - GOWTHAM-OFFICIAL-PGN
    - Diego Perez
    - Zaid Sabih
    - Kunal Mangalorekar
    - Dimitris Kalopisis

# Developed By
Avyukt Framework is made with ❤️ by **Vedant Bhalgama**.
