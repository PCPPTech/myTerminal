import os
import shutil
from myTerminal_installer import list_of_paths_path





# todo
# check if the mtpaths.txt can be overwritten
# Add ls | filter command that basically lists every file in a current or given directory containing the name that comes after "filter".
# Mission: medium


COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_BLUE = "\033[34m"
COLOR_PINK = "\033[95m"
COLOR_MAGENTA = "\033[35m"
COLOR_BLACK = "\033[30m"
COLOR_WHITE_STRONG = "\033[97m"
COLOR_WHITE = "\033[37m"

user_pref_input = COLOR_BLUE # default: BLUE


RESET = "\033[0m"
BOLD = "\033[1m"

try:
    from tkinter import *
except ModuleNotFoundError:
    print(f"{COLOR_GREEN}Installing Module TKINTER{RESET}")
    os.system("pip install tkinter")

from tkinter import *

installation_path = ""

def rmdir_process():
    filename = command[6:]
    if len(filename) <= 0:
        print(f"{COLOR_BLUE}Usage:{RESET} rmdir [DIRNAME]")
        print()
        print()
    try:
        if os.path.isdir(filename):
            os.rmdir(filename)
        else:
            if len(filename) <= 0:
                pass
            else:
                print(f"Please enter a {COLOR_RED}directory{RESET} path. Incase of files, use '{COLOR_GREEN}rm{RESET}'\n\n")
                
                
    except FileNotFoundError:
        print(f"File {COLOR_RED}{filename}{RESET} doesn't exist. \n\n")
        
        
    except OSError:
        shutil.rmtree(filename)
        print(f"Directory `{filename}` was successfully {COLOR_GREEN}removed{RESET}. \n\n")
        print()
        
# extracting info
try:
    with open(list_of_paths_path, "r+") as file:
        lines = file.readlines()
        installation_path = lines[0].strip()
except FileNotFoundError:
    print("please run `myTerminal_installer.py` before this file.")

def clear():
    print("\033[H\033[J", end="")

working_directory = ""
os.system("cls")
try:
    
    print("Welcome to myTerminal.")
    print("Made by Eidnoxon, 2025-2025. Use the code for whatever you want lol just give credits. pls :,c")
    command = 0
    os.chdir(installation_path+"\\home") # Default work-path
    while command != exit:
        # # global user_pr
        working_directory = os.getcwd()
        command=input(f"MT {COLOR_BLUE}{BOLD}{working_directory}\n      ┕━━━━━━━━{RESET}{COLOR_RED}${RESET} ") # User input (looped)
        if command.lower() in ['cls', 'clear']:
            print("\033[H\033[J", end="")
    
        elif command == "help":
            print("Commands:")
            print(f"{COLOR_GREEN}ls{RESET} - List everything in your current directory")
            print(f"         ┕━━━━━ {COLOR_GREEN}ls{RESET} {COLOR_RED}-dir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Lists everything in the given directory.")
            print(f"{COLOR_GREEN}print-txt{RESET} {COLOR_BLUE}[TEXT]{RESET} - prints the text you put after the command.")
            print(f"{COLOR_GREEN}clear{RESET}, {COLOR_GREEN}cls{RESET} - clears the terminal")
            print(f"{COLOR_GREEN}exit{RESET} - terminate the program running process")
            print(f"{COLOR_GREEN}touch{RESET} {COLOR_BLUE}[FILENAME]{RESET} - creates a file with the specified filename")
            print(f"{COLOR_GREEN}cat{RESET} {COLOR_BLUE}[FILENAME]{RESET} - View file content. Won't work on directories.")
            print(f"{COLOR_GREEN}more{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Same as {COLOR_RED}cat{RESET} lolz :3")
            print(f"{COLOR_GREEN}cd{RESET} {COLOR_BLUE}[PATH]{RESET} or {COLOR_BLUE}..{RESET} - changes directory to given path. `cd ..` will go back a directory.")
            print(f"{COLOR_GREEN}rm{RESET} {COLOR_BLUE}[FILENAME]{RESET} - removes a file with the specified filename")
            print(f"{COLOR_GREEN}rmdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - removes a directory with the specified name")
            print(f"{COLOR_GREEN}mkdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - creates a directory with the specified name")
            print(f"{COLOR_GREEN}about myTerminal{RESET} - Displays information about the terminal.")
            print()
            print()
    
        elif command == "ls": # LS COMMAND AND ITS ALGORITHM
            if len(os.listdir()) > 0:
                print()
                print(f"{COLOR_GREEN} The content of {working_directory}:{RESET}")
                for i in os.listdir():
                    if os.path.isdir(i):
                        print(f"[FOLDER] {i}")
                    else:
                        print(f"         {i}")
n(os.listdir()) <= 0: # idk how it can be less than zero but just in case yk :3
 \             
            print()

        elif command.strip().startswith("print-txt"):
            text_to_print = command[10: ]
            print(f"{text_to_print}\n\n")
    
        elif command == 'pwd':
            print(f"{working_directory} \n\n")
            
        elif command == 'exit':
            quit()

        elif command.strip().startswith('touch'):
            filename = command[len('touch '):]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} touch [FILENAME]")
                print()
            else:
                with open(filename, "a+") as file:
                    pass
                print(f"File '{COLOR_GREEN}{filename}{RESET}' was created successfully.")
                print()
        elif command.strip().startswith('rm'):
            if command.strip().startswith('rmdir') == False:
                filename = command[3:]
                try:
                    if len(filename) <= 0:
                        print(f"{COLOR_BLUE}Usage:{RESET} rm [FILENAME]")
                        print()
                    else:
                        os.remove(filename)
                        print(f"File '{COLOR_RED}{filename}{RESET}' was removed successfully.")
                        print()
                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.")
                    print()
                except IsADirectoryError:
                    os.rmdir(filename)
                    print(f"Directory '{COLOR_RED}{filename}{RESET}' was removed successfully.")
                    print()
            elif command.strip().startswith("rmdir"):
                rmdir_process()
        elif command.strip().startswith('more'):
            filename = command[5:]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} more [FILENAME]")
                print()
            else:
                try:
                    with open(filename, "r+") as f:
                        for i in f.readlines():
                            print(i)
                    print()
                    print()
                except IsADirectoryError:
                    print(f'The command {COLOR_BLUE}"more"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.')
                    print()
                    print()
                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.")
                    print()
                    print()
        

        elif command.strip().startswith("cat"):
            filename = command[4:]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} cat [FILENAME]")
                print()
            else:
                if os.path.isdir(filename) == False:
                    try:
                        with open(filename, "r") as f:
                            for i in f.readlines():
                                print(i)
                    except PermissionError:
                        print(f"Access {COLOR_RED}Denied{RESET}.")
                        print()
                        print()
                    except FileNotFoundError:
                        print(f"File `{COLOR_GREEN}{filename}{RESET}` doesn't exist.")
                        print()
                        print()
                else:
                    print(f'The command {COLOR_BLUE}"cat"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.')
                    print()
                    print()

        elif command.strip().startswith("mkdir"):
            dirname = command[6:]
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} mkdir [DIRNAME]")
                print()
                print()
            else:
                os.makedirs(dirname, exist_ok=True)
                print(f"Directory was made {COLOR_GREEN}successfully{RESET}.")
                print()
                print()

        elif command.strip().startswith("ls -dir"):
            dirname = command[8:]
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} ls -dir [DIRNAME]")
                print()
            try:
                if os.path.isdir(dirname):
                    original_dir = os.getcwd()
                    os.chdir(dirname)
                    print(f"Contents of {COLOR_GREEN}{os.getcwd()}{RESET}")
                    for i in os.listdir():
                        if os.path.isdir(i):
                            print(f"[FOLDER] {i}")
                        else:
                            print(f"         {i}")
                    if len(os.listdir()) <= 0:
                        print(f"there are no {COLOR_RED}Directories{RESET} or {COLOR_RED}Files{RESET} found in {COLOR_GREEN}{working_directory}{RESET}")
                        print()
                    os.chdir(original_dir)
                else:
                    print(f"Please specify a {COLOR_RED}Directory{RESET} name.")
                    print()
            except FileNotFoundError:
                print("Given directory doesn't exist.")
                print()


        elif command.strip().startswith("cd"):
            path = command[3:].strip()

            if path == "":
                print(f"{COLOR_BLUE}Usage:{RESET} cd [PATH] or '..' to go back.")
                print()
                print()
            else:
                if path != "..":
                    try:   
                        os.chdir(path)
                        print()
                    except FileNotFoundError:
                        print(f"Path {COLOR_RED}{path}{RESET} doesn't exist.")
                        print()
                        print()
                    except NotADirectoryError:
                        print(f"Path {COLOR_RED}{path}{RESET} is not a directory.")
                        print()
                        print()
                    except OSError:
                        new_path = path.replace('"', "")
                        os.chdir(new_path)
                elif path == "..":
                    try:
                        os.chdir(path)
                        print()
                    except OSError:
                        print("Can't go back any further.")
                        print()
                        print()
        elif command.lower() == "about myterminal":
            print(f"{COLOR_GREEN}myTerminal{RESET} was made by {COLOR_GREEN}Eidnoxon{RESET}, Otherwise known as {COLOR_BLUE}PCPPTech{RESET}.")
            print(f"This project was created to {BOLD} enhance my programming skills and help others.{RESET}")
            print(f"YES!! {COLOR_GREEN}You can use this code for your startup, or your projects!{RESET}")
            print(f"Just please give credits ;P")
            print(f"The code might be a 'little' bit messy, im the worst programmer tbh, but feel free to modify it to your liking!")
            print(f"{COLOR_GREEN}Eidnoxon (PCPPTech) Out, bye :3{RESET}")
            print(f"IF YOU TRY TO USE COMMANDS LIKE NVIM, PYTHON ETC. IT WILL SHOW A POWERSHELL ERROR {COLOR_RED}IF{RESET} IT WILL SHOW ANY")
            print(f"The reason for that is simply: im stupid and I don't know how to implement nvim into my own terminal :3")
            print(f"Any help is appreciated, I want to learn from my mistakes and become better day-by-day 🙏")
            print(f"I {COLOR_RED}PROMISE, ON MY LIFE{RESET} that the rest of the commands are original, and not os.system(command) 🙏")
            print(f"Check the {COLOR_GREEN}code{RESET} if you want to, modify it even, i dont really care :D")
            print(f"You can find me on discord: {COLOR_RED}eidnoxon{RESET}. You are always welcome to friend me :D")

        # customization part (user freewill)
        elif command.lower() == "setcolor":
            def check(var1, var2):
                if var1 == var2:
                    return True
                else:
                    return False
    

            while True: # nested while loops
                clear()
                print("Welcome to the design settings!")
                print("Tell me, which part of the terminal's color do you want to customize?")
                print("1. Command Input")
                print("2. Coming soon (maybe :3)")
                ans = int(input("Answer: "))
                if ans == 1:
                    while colorCommand != "back": # if color command is equals to "back", break the loop
                        clear()
                        print(f"MT {user_pref}{BOLD}{working_directory}\n      ┕━━━━━━━━{RESET}{COLOR_RED}${RESET} ")
                        print("Options:")
                        print("1. Green")
                        print("2. Blue")
                        print("3. Red")
                        print("4. Magenta")
                        print("5. Pink")
                        colorCommand = int(input("Your preference (in nums): "))
                        if colorCommand == "1":
                            if check(user_pref, COLOR_GREEN):
                                print("You already have that selected.")
                            else:
                                user_pref = COLOR_GREEN
                                print(f"{COLOR_GREEN}Color GREEN{RESET} is successfully set.")
                                break
                        elif colorCommand == "2":
                            if check(user_pref, COLOR_BLUE):
                                print("You already have that selected.")
                            else:
                                user_pref = COLOR_BLUE
                                print(f"{COLOR_BLUE}Color BLUE{RESET} is successfully set.")
                                break

                else:
                    print("invalid option.")
                    input()

            """
            def opt_green():
                user_pref = COLOR_GREEN
            def opt_blue():
                user_pref = COLOR_BLUE
            def opt_red():
                user_pref = COLOR_RED
            def opt_magenta():
                user_pref = COLOR_MAGENTA
            def opt_pink():
                user_pref = COLOR_PINK
            



            
            window = Tk()
            # centrize window
            sw = window.winfo_screenwidth() # gets user's screen width (e.g. 1920x1080 monitor's width would be 1920)
            sh = window.winfo_screenheight() # gets user's screen height (the same example, height would be 1080)

            w = 1100 # the tkinter window's width value
            h = 700 # the tkinter window's height value
            x = (sw - w) // 2 # Algorithm to calculate X coordinate
            y = (sh - h) // 2 # Algorithm to calculate Y coordinate

            window.geometry(f"{w}x{h}+{x}+{y}") # Apply given width and height value + the calculated coordinates to centrize window
            window.title("myTerminal - Customization") # title
            window.resizable(False, False) # disables resizability

            # defining widgets
            label_inputCust = Label(window, text="Your input customization:", font=("Consolas", 13))
            showcase_inputCust = Label(window, text=f"{COLOR_BLUE}{BOLD}{working_directory}\n      ┕━━━━━━━━{RESET}{COLOR_RED}${RESET}", font=("Consolas", 13))
            button_green = Button(window, text="Green", font=("Consolas", 12), command=opt_green)
            button_blue = Button(window, text="Blue", font=("Consolas", 12), command=opt_blue)
            button_red = Button(window, text="Red", font=("Consolas", 12), command=opt_red)
            button_magenta = Button(window, text="Magenta", font=("Consolas", 12), command=opt_magenta)
            button_pink = Button(window, text="Pink", font=("Consolas", 12), command=opt_pink)

            # packing labels and buttons (temporary, its design is hella ugly)
            label_inputCust.pack()
            showcase_inputCust.pack()

            button_green.pack()
            button_blue.pack()
            button_red.pack()
            button_magenta.pack()
            button_pink.pack()

            window.mainloop()
            """

        else:
            if shutil.which(command):
                os.system(command)
            else:
                print(f'"{COLOR_RED}{command}{RESET}" is not a valid command. If you\'re stuck, please type in {COLOR_GREEN}"help"{RESET}\n\n')



except FileNotFoundError:
    print(f"{COLOR_RED}Please run `python myTerminal_installer.py` or doubleclick the myTerminal_intaller.py file before continuing.{RESET}")

except KeyboardInterrupt:
    print("CTRL + C is faster i guess. I hope youll be back :D")
