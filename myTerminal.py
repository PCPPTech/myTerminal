from tkinter import *
import os
import shutil
import textwrap
import time
from myTerminal_installer import list_of_paths_path
import sys
import socket

COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_BLUE = "\033[34m"
COLOR_PINK = "\033[95m"
COLOR_MAGENTA = "\033[35m"
COLOR_BLACK = "\033[30m"
COLOR_WHITE_STRONG = "\033[97m"
COLOR_WHITE = "\033[37m"


RESET = "\033[0m"
BOLD = "\033[1m"

# check for flags
if len(sys.argv) > 1:
    if sys.argv[1] == "--version":
        print("version 1.1.0")
        quit()
    elif sys.argv[1] == "--about":
        print("This is an open source terminal project made simply for fun by Eidnoxon(PCPPTech).\n")
        quit()
    else:
        print(f"{COLOR_GREEN}--version{RESET}: displays the version of myTerminal.")
        print(f"{COLOR_GREEN}--about{RESET}: displays information about myTerminal.")
else:
    pass

user_pref_if = "" # `if` is short for `input field` in this case


# TODO TODO TODO TODO
# Clear up dictionary
# make setcolor command work

user_pref_input = 0
user_pref_ds = 0
color_dict = {
    "GREEN": COLOR_GREEN,
    "BLUE": COLOR_BLUE,
    "RED": COLOR_RED,
    "PINK": COLOR_PINK,
    "MAGENTA": COLOR_MAGENTA,
    "BLACK": COLOR_BLACK,
    "WHITE": COLOR_WHITE_STRONG
}


os.chdir(f"C:\\Users\\{os.getlogin()}")
try:
    with open("mt_data.txt", "r+") as file: # if it doesnt exist, make it
        lines = file.readlines()
        if len(lines) <= 0:
            user_pref_input = COLOR_BLUE
            file.write("BLUE")
        else:
            saved_color = lines[0].strip()
            if saved_color in color_dict:
                user_pref_input = color_dict[saved_color]
            else:
                user_pref_input = COLOR_BLUE # default
except FileNotFoundError:
    with open("mt_data.txt", "a+") as file:
        file.write("BLUE")

try:
    with open("mt_datadollarsign.txt", "r+") as file:
        lines = file.readlines()
        if len(lines) <= 0:
            user_pref_ds = COLOR_RED
            file.write("RED")
        else:
            saved_color = lines[0].strip()
            if saved_color in color_dict:
                user_pref_ds = color_dict[saved_color]
            else:
                user_pref_ds = COLOR_RED
except FileNotFoundError:
    with open("mt_datadollarsign.txt", "a+") as file:
        file.write("RED")



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
    with open(list_of_paths_path, "r") as file:
        lines = file.readlines()
        installation_path = lines[0].strip()
except (FileNotFoundError, IndexError):
    print("please run `myTerminal_installer.py` before this file.")


def clear():

    print("\033[H\033[J", end="")



os.system("cls")
try:
    print("Welcome to myTerminal.")
    print("Made by Eidnoxon, 2025-2025. Use the code for whatever you want lol just give credits. pls :,c")
    print("I am sorry if this app is full of bugs, i tried my best")
    command = 0
    os.chdir(installation_path+"\\home")  # Default work-path
    while command != exit:
        # User input (looped)
        # command = input(f"MT {user_pref_input}{BOLD}{working_directory}\n      ┕━━━━━━━━{RESET}{user_pref_ds}${RESET} ")
        
        working_directory = os.getcwd()

        # user input field preference information extraction
        userPrefDict = {
            1: f"MT {user_pref_input}{BOLD}zaworkdir\\n\\t\\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET}",
            2: f"MT {user_pref_input}{BOLD}zaworkdir{RESET}{user_pref_ds}>{RESET}",
            3: f"MT {user_pref_input}{BOLD}zaworkdir{RESET}{user_pref_ds}~${RESET}",
            4: f"MT ╭─ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET}\\n   ╰─ {user_pref_ds}${RESET}",
            5: f"MT ┌─[{user_pref_input}{BOLD}zaworkdir{RESET}]\\n   └─ {user_pref_input}${RESET}",
            6: f"MT [ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET} {user_pref_input}{BOLD}zaworkdir{RESET} ] {user_pref_ds}${RESET}",
            7: f"MT < {user_pref_input}{os.getlogin()}{RESET}@{user_pref_input}{BOLD}zaworkdir{RESET} > {user_pref_ds}${RESET}"
        }

        try:
            with open(f"C:\\Users\\{os.getlogin()}\\mt_userinputfield.txt", "r", encoding='utf-8') as file:
                file.seek(0)
                lines = file.readlines()
                if lines:
                    user_pref_if = lines[0]
                else:
                    user_pref_if = userPrefDict[1]
        except FileNotFoundError:
            user_pref_if = userPrefDict[1] # default value
        
        user_pref_if = user_pref_if.replace("\\n", "\n").replace("\\t", "\t").replace("zaworkdir", working_directory)

        command = input(f"{user_pref_if} ")
        if command.lower() in ['cls', 'clear']:
            print("\033[H\033[J", end="")

        elif command.lower() == "help":
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
                {COLOR_GREEN}setcolor{RESET} - Displays a menu where you can customize the color of different parts in the input field
                {COLOR_GREEN}sif{RESET} - Stands for `{COLOR_BLACK}set input field{RESET}`, displays a menu where you can customize the input field.
                \n\n
            """))

        elif command.lower() == "ls":  # LS COMMAND AND ITS ALGORITHM
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
                print(f"\n\t\tThis directory is {COLOR_RED}empty{RESET}.\n\n")

        elif command.lower().strip().startswith("print-txt"):
            text_to_print = command[10:]
            print(f"{text_to_print}\n\n")

        elif command.lower() == 'pwd':
            print(f"{working_directory}\n\n")

        elif command.lower() == 'exit':
            quit()

        elif command.lower().strip().startswith('touch'):
            filename = command[len('touch '):]
            if len(filename) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} touch [FILENAME]\n")
            else:
                with open(filename, "a+") as file:
                    pass
                print(f"File '{COLOR_GREEN}{filename}{RESET}' was created successfully.\n")

        elif command.lower().strip().startswith('rm'):
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

        elif command.lower().strip().startswith('more'):
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

        elif command.lower().strip().startswith("cat"):
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

        elif command.lower().strip().startswith("mkdir"):
            dirname = command[6:]
            if len(dirname) <= 0:
                print(f"{COLOR_BLUE}Usage:{RESET} mkdir [DIRNAME]\n\n")
            else:
                os.makedirs(dirname, exist_ok=True)
                print(f"Directory was made {COLOR_GREEN}successfully{RESET}.\n\n")

        elif command.lower().strip().startswith("ls -dir"):
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

        elif command.lower().strip().startswith("cd"):
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
                Feel free to friend me on {COLOR_PINK}Discord{RESET}: {COLOR_RED}eidnoxon{RESET}
                {COLOR_GREEN}Eidnoxon (PCPPTech) Out, bye :3{RESET}
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
                    2. Dollarsign Customization
                """))
                ans = input("Enter a number, or 'exit' to quit: ")
                if ans == '1':
                    # Color dictionary, numbers are "keys" and the values are tuples with a string and color code
                    color_options = { # rpd, you can use a dictionary
                        "1": ("GREEN", COLOR_GREEN),
                        "2": ("BLUE", COLOR_BLUE),
                        "3": ("RED", COLOR_RED),
                        "4": ("PINK", COLOR_PINK),
                        "5": ("WHITE", COLOR_WHITE_STRONG),
                        "6": ("GRAY", COLOR_BLACK)
                    }
                    colorCommand = "" # value is the key in the dictionary
                    selected_color_name = "" # value from the color name portion of the dictionary
                    while colorCommand != "back":  # if color command is equals to "back", break the loop
                        clear()


                        # Build the dynamic color menu from the dictionary
                        menu = f"MT {user_pref_input}{BOLD}{working_directory}\n"
                        menu += f"\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET}\n" # the += concatinates the strings together, print() will render the longer string
                        menu += "Options:\n"
                        for key, (name, color) in color_options.items():
                            menu += f"  {key}. {name.capitalize()}{RESET}\n" # .capitalize() just capitilizes the first char in the string, rest are lowercase
                            # menu += f"  {key}. {color}{name.capitalize()}{RESET}\n" # if you want the text to be those colors too (magenta doesn't show for some reason)
                        menu += "  Type 'back' or 'done' to finish.\n"
                        print(menu)

                        colorCommand = input(
                            "Your preference (in nums): "
                        )
                        if colorCommand.lower() == "done":
                            temp_var = working_directory
                            os.chdir(f"C:\\Users\\{os.getlogin()}")
                            with open("mt_data.txt", "a+") as file:
                                file.seek(0)
                                lines = file.readlines()
                                if lines:
                                    file.truncate(0)
                                file.write(selected_color_name)
                            os.chdir(temp_var)
                            break

                        elif colorCommand in color_options:
                            name, value = color_options[colorCommand]
                            if check(user_pref_input, value):
                                print("You already have that selected.\n")
                                time.sleep(2)
                            else:
                                user_pref_input = value
                                selected_color_name = name
                                print(f"{value}Color {name}{RESET} is successfully set.")
                                time.sleep(2)
                        elif colorCommand.lower() == "back":
                            break
                        else:
                            print("Invalid option. Please choose a valid number or type 'back'.")
                            time.sleep(2)
                        
                elif ans == '2':
                    color_options = { # rpd, you can use a dictionary
                        "1": ("GREEN", COLOR_GREEN),
                        "2": ("BLUE", COLOR_BLUE),
                        "3": ("RED", COLOR_RED),
                        "4": ("PINK", COLOR_PINK),
                        "5": ("WHITE", COLOR_WHITE_STRONG),
                        "6": ("GRAY", COLOR_BLACK)
                    }
                    colorCommand = "" # value is the key in the dictionary
                    selected_color_name = "" # value from the color name portion of the dictionary
                    while colorCommand != "back":  # if color command is equals to "back", break the loop
                        clear()


                        # Build the dynamic color menu from the dictionary
                        menu = f"MT {user_pref_input}{BOLD}{working_directory}\n"
                        menu += f"\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET}\n" # the += concatinates the strings together, print() will render the longer string
                        menu += "Options:\n"
                        for key, (name, color) in color_options.items():
                            menu += f"  {key}. {name.capitalize()}{RESET}\n" # .capitalize() just capitilizes the first char in the string, rest are lowercase
                            # menu += f"  {key}. {color}{name.capitalize()}{RESET}\n" # if you want the text to be those colors too (magenta doesn't show for some reason)
                        menu += "  Type 'back' or 'done' to finish.\n"
                        print(menu)

                        colorCommand = input(
                            "Your preference (in nums): "
                        )
                        if colorCommand.lower() == "done":
                            temp_var = working_directory
                            os.chdir(f"C:\\Users\\{os.getlogin()}")
                            with open("mt_datadollarsign.txt", "a+") as file:
                                file.seek(0)
                                lines = file.readlines()
                                if lines:
                                    file.truncate(0)
                                file.write(selected_color_name)
                            os.chdir(temp_var)
                            break

                        elif colorCommand in color_options:
                            name, value = color_options[colorCommand]
                            if check(user_pref_ds, value):
                                print("You already have that selected.\n")
                                time.sleep(2)
                            else:
                                user_pref_ds = value
                                selected_color_name = name
                                print(f"{value}Color {name}{RESET} is successfully set.")
                                time.sleep(2)
                        elif colorCommand.lower() == "back":
                            break
                        else:
                            print("Invalid option. Please choose a valid number or type 'back'.")
                            time.sleep(2)
                elif ans == 'exit':
                    break

                else:
                    print("invalid option.")
                    input()
        elif len(command) == 0:
            pass # if the string is empty; don't do anything
        elif command.lower() == "sif":
            
            while True:
                print(f"""
                1. MT {user_pref_input}{BOLD}{working_directory}\n\t\t\t┕━━━━━━━━{RESET}{user_pref_ds}${RESET} - {COLOR_BLUE}Kali Linux{RESET} inspired design
                2. MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}>{RESET} - Classic Terminal
                3. MT {user_pref_input}{BOLD}{working_directory}{RESET}{user_pref_ds}~${RESET} - Classic Linux
                
                -- BOX-LIKE DESIGNS --

                4. MT ╭─ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET}
                      ╰─ {user_pref_ds}${RESET}
                
                5. MT ┌─[{user_pref_input}{BOLD}{working_directory}{RESET}]
                      └─ {user_pref_input}${RESET}

                6. MT [ {user_pref_input}{os.getlogin()}{RESET}@{COLOR_RED}{socket.gethostname()}{RESET} {user_pref_input}{BOLD}{working_directory}{RESET} ] {user_pref_ds}${RESET}
                7. MT < {user_pref_input}{os.getlogin()}{RESET}@{user_pref_input}{BOLD}{working_directory}{RESET} > {user_pref_ds}${RESET}
                """)
                userinp = int(input("\nType the number 8 to exit\n> "))
                if userinp in [1, 2, 3, 4, 5, 6, 7]:
                    thing_to_write = ""
                    with open(f"C:\\Users\\{os.getlogin()}\\mt_userinputfield.txt", "a+", encoding="utf-8") as file:
                        file.seek(0)
                        lines = file.readlines()
                        if lines:
                            file.truncate(0)
                        thing_to_write = userPrefDict[userinp]
                        file.write(thing_to_write)
                    print(f"{userPrefDict[userinp].replace("\\n", "\n").replace("\\t", "\t")} successfully applied. Restart the terminal to see the effects.")
                    break
                elif userinp == 8:
                    clear()
                    break
                else:
                    print("Invalid Option, Try again.")
                    break
        else:
            cmd = command.split()[0]
            if shutil.which(cmd):
                os.system(command)
            else:
                print(f'"{COLOR_RED}{command}{RESET}" is not a valid command. If you\'re stuck, please type in {COLOR_GREEN}"help"{RESET}\n\n')

except FileNotFoundError:
    print(f"{COLOR_RED}Please run `python myTerminal_installer.py` or doubleclick the myTerminal_intaller.py file before continuing.{RESET}")

except KeyboardInterrupt:
    print("CTRL + C is faster i guess. I hope youll be back :D")
