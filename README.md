# myTerminal

A simple, custom terminal environment with a graphical installer and basic command support.  
Created by **Eidnoxon (PCPPTech)** in 2025 as a fun and educational project.  
You are free to use or modify the code — just give credits

---

## Project Structure

```
myTerminal/
├── myTerminal_installer.py   # GUI-based installer to set up your terminal path
├── myTerminal_main.py        # The terminal itself, with custom commands
```

---

## Features

- Cross-platform-ish terminal emulator using Python and `tkinter`
- Basic shell-like commands:
  - `ls`, `cd`, `mkdir`, `rm`, `rmdir`, `touch`, `cat`, `more`
  - `clear`, `help`, `exit`, `about myTerminal`
- Customization options (colors, input styling)
- `.mtpaths.txt` to store install location
- Graphical setup wizard to choose install directory

---

## Requirements

- Python 3.x
- `tkinter` (will be installed automatically if missing)

---

## Getting Started

1. **Run the installer:**

   ```bash
   python myTerminal_installer.py
   ```

2. **Then run the terminal:**

   ```bash
   python myTerminal_main.py
   ```

---

## Customization

- You can customize the colors by using the `setcolor` command inside the terminal.
- You can also customize the input field by using the `sif` (`set input field`) command inside the terminal.
---

## Supported Commands (from inside the terminal)


| Command            | Description                                                      |
| ------------------ | -----------------------------------------------------------------|
| `help`             | Shows command list                                               |
| `ls`               | Lists files in current directory                                 |
| `ls -dir [dir]`    | Lists contents of specified directory                            |
| `cd [path]`        | Changes directory                                                |
| `touch [name]`     | Creates a new file                                               |
| `mkdir [name]`     | Creates a new directory                                          |
| `rm [file]`        | Deletes a file                                                   |
| `rmdir [dir]`      | Deletes a directory (recursively if needed)                      |
| `cat [file]`       | Prints contents of a file                                        |
| `more [file]`      | Same as `cat`                                                    |
| `print-txt [txt]`  | Echoes the provided text                                         |
| `pwd`              | Shows current directory                                          |
| `clear` / `cls`    | Clears the screen                                                |
| `about myTerminal` | Info about the project                                           |
| `sif`              | Stands for `set input field`, allows input field customization.  |
| `setcolor`         | Allows color customization in different parts of the input field.|
---

## Notes

- If `myTerminal_main.py` fails to run, ensure you have already run the installer.
- Windows paths (e.g., `C:\\Users\\[username]\\`) are automatically handled.
- Terminal attempts to use ANSI colors — best viewed in compatible terminals (e.g., CMD, Powershell, VSCode terminal).

---

## Developer Notes

- Code is written for fun and learning. Contributions or suggestions are welcome.
- You can friend the creator on Discord: `eidnoxon`

---

## License

Open-source, use it for whatever — just credit **Eidnoxon (PCPPTech)**

---

## Errors and their reasons
- `PermissionError`, or `Can't ...: Insufficient Permission`.
- This error pretty much explains itself: It means that it can't do a certain operation because of the lack of permission. It can often be caused by e.g. trying to remove a folder while the folder is under use by another app.
I integrated a lot of PermissionError handling lines, so it will most likely won't make you exit the CLI once you encounter that error.
- `FileNotFoundError`.
- You encounter this error when trying to remove a file or a directory that `doesn't exist`. If you encounter this error when you try to run `myTerminal.py` and you even ran `myTerminal_installer.py` beforehand, the issue might be
that your home directory isn't `C:/Users/[username]`. `myTerminal` creates all the text files that are used to store the user's customization data in `C:/Users/[username]`. Why? Because it is easily accessable.
