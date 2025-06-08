
import os
list_of_paths_path = f"C:\\Users\\{os.getlogin()}\\mtpaths.txt"

try:
    from tkinter import *
except ModuleNotFoundError:
    os.system("pip install tkinter")

from tkinter import * # rpd: not required since you already did that, should be included in the exception though

given_installation_path = ""
installation_path_final = ""
mthome_path = ""
with open(f"C:\\Users\\{os.getlogin()}\\mtpaths.txt", "a+") as file:
    pass # Create the text file if it doesnt already exist
# create a mtdata_dollarsign.txt file to store the color of the dollar sign
with open(f"C:\\Users\\{os.getlogin()}\\mt_datadollarsign.txt", "a+") as file:
    pass

def main():
    global given_installation_path
    global installation_path_final
    global mthome_path
    def centrize(width, height, rootname, resizable_bool, title):
        sw = rootname.winfo_screenwidth()
        sh = rootname.winfo_screenheight()

        x = (sw - width) // 2
        y = (sh - height) // 2

        rootname.geometry(f"{width}x{height}+{x}+{y}")
        rootname.resizable(resizable_bool, resizable_bool)
        rootname.title(title)

    def submitted_INSTALLATIONPATH(event=None):

        global installation_path_final
        given_path = installation_path.get()
        installer_window.destroy()
        if given_path == default_installation_path:
            installation_path_final = default_installation_path
        else:
            installation_path_final = given_path
    
        # my brain hurts please help
        os.makedirs(f"{installation_path_final}", exist_ok=True)
        os.makedirs(f"{installation_path_final}\\home", exist_ok=True)

        success = Tk()
        success.configure(bg='black')
        centrize(600, 200, success, False, 'Installation Success!')

        label=Label(success, text="Installation was successful.", bg='black', fg='green')
        label.pack()
    

        success.mainloop()


    global mthome_path
    default_installation_path = f"C:\\Users\\{os.getlogin()}\\.mThome"
    mthome_path = f"{installation_path_final}\\.mThome\\home"

    installer_window = Tk()
    centrize(800, 500, installer_window, False, "Installer")

    label = Label(installer_window, text="Specify installation path:", font=("Arial", 12))
    installation_path = Entry(installer_window, font=("Times New Roman", 12), width=400)
    installation_path.insert(0, default_installation_path)
    submit_Button = Button(installer_window, text="Done", font=("Arial", 12), command=submitted_INSTALLATIONPATH)

#pack widgets

    label.pack()
    installation_path.pack()
    submit_Button.pack()

    installation_path.bind("<Return>", submitted_INSTALLATIONPATH)

    installer_window.mainloop()

if __name__ == "__main__":
    main()
    os.chdir(f"{installation_path_final}")
    with open(list_of_paths_path, "a+") as file:
        lines = file.readlines()
        if len(lines) > 0:
            file.truncate(0)
            file.write(installation_path_final)
        else:
            file.write(installation_path_final + "\n")

    os.chdir(f"C:\\Users\\{os.getlogin()}")
    with open("mt_data.txt", "a+") as f:
        lines = f.readlines()

