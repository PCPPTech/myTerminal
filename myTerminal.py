from tkinter import *
import os
import shutil
import textwrap
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

user_pref_input = 0

os.chdir(f"C:\\Users\\{os.getlogin()}")
with open("mt_data.txt", "a+") as file: # if it doesnt exist, make it
    lines = file.readlines()
    if len(lines) <= 0:
        user_pref_input = COLOR_BLUE # default
    else:
        user_pref_input = lines[0] # i will always write it in the first line
        # if it is modified, the code won't work. IF YOU CAN DO ANYTHING ABOUT, PLEASE DO
        # - Eidnoxon

RESET = "\033[0m"
BOLD = "\033[1m"


try:
    from tkinter import *
except ModuleNotFoundError:
    print(f"{COLOR_GREEN}Installing Module {BOLD}TKINTER{RESET}")
    os.system("pip install tkinter")


installation_path = ""


def rmdir_process():
    filename = command[6:]
    if len(filename) <= 0:
        print(f"{COLOR_BLUE}Usage:{RESET} rmdir [DIRNAME]\n\n")
    try:
        if os.path.isdir(filename):
            os.rmdir(filename)
        else:
            if len(filename) <= 0:
                pass
            else:
                print(f"Please enter a {COLOR_RED}directory{RESET} path. Incase of files, use '{COLOR_GREEN}rm{RESET}'\n\n")

    except FileNotFoundError:
        print(f"File {COLOR_RED}{filename}{RESET} doesn't exist.\n\n")

    except OSError:
        shutil.rmtree(filename)
        print(f"Directory `{filename}` was successfully {COLOR_GREEN}removed{RESET}.\n\n")


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
    os.chdir(installation_path+"\\home")  # Default work-path
    while command != exit:
        # global user_pref_input
        working_directory = os.getcwd()
        # User input (looped)
        command = input(
            f"MT {user_pref_input}{BOLD}{working_directory}\n      ┕━━━━━━━━{RESET}{COLOR_RED}${RESET} ")
        if command.lower() in ['cls', 'clear']:
            print("\033[H\033[J", end="")

        elif command == "help":
            print(textwrap.dedent(
                f"""\
                Commands:
                {COLOR_GREEN}ls{RESET} - List everything in your current directory
                \t┕━━━━━ {COLOR_GREEN}ls{RESET} {COLOR_RED}-dir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Lists everything in the given directory.
                {COLOR_GREEN}print-txt{RESET} {COLOR_BLUE}[TEXT]{RESET} - Prints the text you put after the command.
                {COLOR_GREEN}clear{RESET}, {COLOR_GREEN}cls{RESET} - Clears the terminal
                {COLOR_GREEN}exit{RESET} - Terminates the program
                {COLOR_GREEN}touch{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Creates a file with the specified filename
                {COLOR_GREEN}cat{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Views file content (won’t work on directories)
                {COLOR_GREEN}more{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Same as {COLOR_RED}cat{RESET} lolz :3
                {COLOR_GREEN}cd{RESET} {COLOR_BLUE}[PATH]{RESET} or {COLOR_BLUE}..{RESET} - Changes directory to the given path (`cd ..` goes back)
                {COLOR_GREEN}rm{RESET} {COLOR_BLUE}[FILENAME]{RESET} - Removes a file
                {COLOR_GREEN}rmdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Removes a directory
                {COLOR_GREEN}mkdir{RESET} {COLOR_BLUE}[DIRNAME]{RESET} - Creates a directory
                {COLOR_GREEN}about myTerminal{RESET} - Displays information about the terminal.
                \n\n
            """))

        elif command == "ls":  # LS COMMAND AND ITS ALGORITHM
            if len(os.listdir()) > 0:
                print()
                print(f"{COLOR_GREEN} The content of {working_directory}:{RESET}")
                for i in os.listdir():
                    if os.path.isdir(i):
                        print(f"[FOLDER] {i}")
                    else:
                        print(f"         {i}")
                print() # new line after LS command finished, so it wont look bad
            else:
                print(f"This directory is {COLOR_RED}empty{RESET}.\n\n")

        elif command.strip().startswith("print-txt"):
            text_to_print = command[10:]
            print(f"{text_to_print}\n\n")

        elif command == 'pwd':
            print(f"{working_directory}\n\n")

        elif command == 'exit':
            quit()

        elif command.strip().startswith('touch'):
            filename = command[len('touch '):]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} touch [FILENAME]\n")
            else:
                with open(filename, "a+") as file:
                    pass
                print(f"File '{COLOR_GREEN}{filename}{RESET}' was created successfully.\n")

        elif command.strip().startswith('rm'):
            if command.strip().startswith('rmdir') == False:
                filename = command[3:]
                try:
                    if len(filename) <= 0:
                        print(f"{COLOR_BLUE}Usage:{RESET} rm [FILENAME]\n")
                    else:
                        os.remove(filename)
                        print(f"File '{COLOR_RED}{filename}{RESET}' was removed successfully.\n")

                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.\n")
                except IsADirectoryError:
                    ans = input("The given filename is a directory. Do you wanna remove it?(y/n) ")
                    if ans.lower() == 'y':
                        os.rmdir(filename)
                        print(f"Directory '{COLOR_RED}{filename}{RESET}' was removed successfully.\n")
                    else:
                        print()
            elif command.strip().startswith("rmdir"):
                rmdir_process()

        elif command.strip().startswith('more'):
            filename = command[5:]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} more [FILENAME]\n")
            else:
                try:
                    with open(filename, "r+") as f:
                        for i in f.readlines():
                            print(f"{i}\n\n")
                except IsADirectoryError:
                    print(f'The command {COLOR_BLUE}"more"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.\n\n')
                except FileNotFoundError:
                    print(f"'{filename}' {COLOR_RED}was not{RESET} found.\n\n")

        elif command.strip().startswith("cat"):
            filename = command[4:]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} cat [FILENAME]\n")
            else:
                if os.path.isdir(filename) == False:
                    try:
                        with open(filename, "r") as f:
                            for i in f.readlines():
                                print(i)
                    except PermissionError:
                        print(f"Access {COLOR_RED}Denied{RESET}.\n\n")
                    except FileNotFoundError:
                        print(f"File `{COLOR_GREEN}{filename}{RESET}` doesn't exist.\n\n")
                else:
                    print(f'The command {COLOR_BLUE}"cat"{RESET} cannot scan directories. Maybe try {COLOR_RED}ls -dir [DIRNAME]{RESET}.\n\n')

        elif command.strip().startswith("mkdir"):
            dirname = command[6:]
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} mkdir [DIRNAME]\n\n")
            else:
                os.makedirs(dirname, exist_ok=True)
                print(f"Directory was made {COLOR_GREEN}successfully{RESET}.\n\n")

        elif command.strip().startswith("ls -dir"):
            dirname = command[8:]
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} ls -dir [DIRNAME]\n")
            try:
                if os.path.isdir(dirname):
                    original_dir = os.getcwd()
                    os.chdir(dirname)
                    print(f"Contents of {COLOR_GREEN}{os.getcwd()}{RESET}")
                    for i in os.listdir():
                        if os.path.isdir(i):
                            print(f"[FOLDER] {i}")
                        else:
                            print(f"\t{i}")
                    if len(os.listdir()) <= 0:
                        print(f"there are no {COLOR_RED}Directories{RESET} or {COLOR_RED}Files{RESET} found in {COLOR_GREEN}{working_directory}{RESET}\n")
                    os.chdir(original_dir)
                else:
                    print(f"Please specify a {COLOR_RED}Directory{RESET} name.\n")
            except FileNotFoundError:
                print("Given directory doesn't exist.\n")

        elif command.strip().startswith("cd"):
            path = command[3:].strip()

            if path == "":
                print(f"{COLOR_BLUE}Usage:{RESET} cd [PATH] or '..' to go back.\n\n")
            else:
                if path != "..":
                    try:
                        os.chdir(path)
                        print()
                    except FileNotFoundError:
                        print(f"Path {COLOR_RED}{path}{RESET} doesn't exist.\n\n")
                    except NotADirectoryError:
                        print(f"Path {COLOR_RED}{path}{RESET} is not a directory.\n\n")
                    except OSError:
                        new_path = path.replace('"', "")
                        os.chdir(new_path)
                elif path == "..":
                    try:
                        os.chdir(path)
                        print()
                    except OSError:
                        print("Can't go back any further.\n\n")

        elif command.lower() == "about myterminal":
            print(textwrap.dedent(
                f"""\
                {COLOR_GREEN}myTerminal{RESET} was made by {COLOR_GREEN}Eidnoxon{RESET}, otherwise known as {COLOR_BLUE}PCPPTech{RESET}.
                This project was created to {BOLD}enhance my programming skills and help others.{RESET}
                YES!! {COLOR_GREEN}You can use this code for your startup, or your projects!{RESET}
                Just please give credits ;P
                The code might be a *little* bit messy — I'm the worst programmer tbh, but feel free to modify it to your liking!
                {COLOR_GREEN}Eidnoxon (PCPPTech) Out, bye :3{RESET}
                IF YOU TRY TO USE COMMANDS LIKE NVIM, PYTHON ETC., IT WILL SHOW A POWERSHELL ERROR {COLOR_RED}IF{RESET} IT SHOWS ANYTHING AT ALL.
                The reason for that is simply: I'm stupid and don't know how to implement nvim into my own terminal :3
                Any help is appreciated — I want to learn from my mistakes and become better day-by-day 🙏
                I {COLOR_RED}PROMISE, ON MY LIFE{RESET} that the rest of the commands are original, and not just os.system(command) 🙏
                Check the {COLOR_GREEN}code{RESET} if you want to. Modify it even — I don’t really care :D
                You can find me on Discord: {COLOR_RED}eidnoxon{RESET}. You’re always welcome to friend me :D
            """))

        # customization part (user freewill)
        elif command.lower() == "setcolor":
            def check(var1, var2):
                if var1 == var2:
                    return True
                else:
                    return False

            while True:  # nested while loops
                clear()
                print(textwrap.dedent(
                    """\
                    Welcome to the design settings!
                    Tell me, which part of the terminal's color do you want to customize?
                    1. Command Input
                    2. Coming soon (maybe :3)
                """))
                ans = input("Answer (type 'exit' to exit): ")
                if ans == '1':
                    colorCommand = ""
                    while colorCommand != "back":  # if color command is equals to "back", break the loop
                        clear()
                        print(textwrap.dedent(
                            f"""\
                            MT {user_pref_input}{BOLD}{working_directory}
                            \t┕━━━━━━━━{RESET}{COLOR_RED}${RESET}
                            Options:
                            1. Green
                            2. Blue
                            3. Red
                            4. Magenta
                            5. Pink
                            6. White
                            7. Black
                        """))
                        colorCommand = input(
                            "Your preference (in nums): "
                        )
                        if colorCommand == "1":
                            if check(user_pref_input, COLOR_GREEN):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_GREEN
                                print(f"{COLOR_GREEN}Color GREEN{RESET} is successfully set.")
                        elif colorCommand == "2":
                            if check(user_pref_input, COLOR_BLUE):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_BLUE
                                print(f"{COLOR_BLUE}Color BLUE{RESET} is successfully set.")
                        elif colorCommand == "3":
                            if check(user_pref_input, COLOR_RED):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_RED
                                print(f"{COLOR_RED}Color RED{RESET} is successfully set.")
                        elif colorCommand == "4":
                            if check(user_pref_input, COLOR_MAGENTA):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_MAGENTA
                                print(f"{COLOR_MAGENTA}Color MAGENTA{RESET} is successfully set.")
                        elif colorCommand == "5":
                            if check(user_pref_input, COLOR_PINK):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_PINK
                                print(f"{COLOR_PINK}Color PINK{RESET} is successfully set.")
                        elif colorCommand == "6":
                            if check(user_pref_input, COLOR_WHITE_STRONG):
                                print("You already have that selected.\n")
                            else:
                                user_pref = COLOR_WHITE_STRONG
                                print(f"{COLOR_WHITE_STRONG}Color WHITE{RESET} is successfully set.")
                        elif colorCommand == "7":
                            if check(user_pref_input, COLOR_BLACK):
                                print("You already have that selected.\n")
                            else:
                                user_pref_input = COLOR_BLACK
                                print(f"{COLOR_BLACK}Color BLACK{RESET} is successfully set.")
                        
                        elif colorCommand.lower() == "done": # TODO TODO TODO TODO ERROR HERE! ERROR HERE!
                            os.chdir(f"C:\\Users\\{os.getlogin()}")
                            with open("mt_data.txt", "a+") as file:
                                lines = file.readlines()
                                if len(lines) >= 1:
                                    file.truncate(0)
                                file.write(str(user_pref_input)) # Sadly, it writes the variable's VALUE and not the NAME :(
                                # Can you fix it? Please? Thanks
                                # - Eidnoxon
                            break

                        else:
                            break
                elif ans == '2':
                    print('bro just be patient\n')
                elif ans == 'exit':
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
