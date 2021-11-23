'''
                █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 　 █▀▀█ █  █ 
                █    █  █ █  █ ▀▀█ █  █ 　 █  █ █▄▄█ 
                █▄▄█ ▀▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀▀ 　 █▀▀▀ ▄▄▄█
                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
'''
import os
import sys
import socket
import psutil
import platform
from datetime import date

color_list = '''
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
'''

cmd_list = '''
    date     - Shows current date
    python   - Execute a python file
    list     - List current directory 
    color    - Changes text color 
    ipc      - Returns IP and HOSTNAME 
    spec     - System specifications
    gendir   - Generate a new directory
    exit     - Exits this program
    cpu?     - Returns current CPU usage
    ram?     - Returns current RAM usage
    '''

os.system("cls")
print(" ©HttpAnand | ConsoPY 1.0.0 | Python 3.10.0 \n Type help for command list\n")
dir = os.getcwd()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
today = date.today()
fmt = today.strftime("%d/%m/%Y")

ip_c = f'''
    HOSTNAME : {hostname}
    LOCAL IP : {ip}
    ''' 
spec = f'''  
    OS: {platform.uname().system}
    OS Version : {platform.uname().version}
    System Name: {platform.uname().node}
    System Type : {platform.uname().machine}
    Processor : {platform.uname().processor}
'''

dt = f'''
    Current date is : {fmt}
'''

ru = f'''
    RAM USAGE :{psutil.virtual_memory().percent}%
'''

cu = f''' 
    CPU USAGE : {psutil.cpu_percent()}%
'''
while True: 

    cmd = input(f'ConsoPY@{dir}:-> ')
    if(cmd == 'clear'):
        os.system("cls")
    elif(cmd == 'python'):
        file_name = input("Enter file name :\n")
        os.system(f"python {file_name}")
    elif(cmd == 'list'):
        print(f'\n{os.listdir(dir)}\n')
    elif(cmd == 'date'):
        print(dt)
    elif('color' in cmd):
        clr = input(f'{color_list} \n  Enter Color : ')
        os.system(f'color {clr}')
    elif(cmd == 'ipc'):
        print(ip_c)
    elif(cmd == 'spec'):
        print(spec)   
    elif(cmd == 'cpu?'):
        print(cu)
    elif(cmd == 'ram?'):
        print(ru)
    elif(cmd == 'gendir'):
        nm = input('Enter name of directory : ')
        os.system(f"mkdir {nm}")
        print(f'{nm} was generated')
    elif(cmd == ''):
        print('')
    elif(cmd == 'help'):
        print(cmd_list)
    elif(cmd == 'exit'):  
        print('------------------------------------')
        sys.exit("Thank You For Using ConsoPY\n------------------------------------")
    else:
        print('No such command | Type help for command list')

       




