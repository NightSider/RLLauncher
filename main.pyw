import helper
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import filedialog
from shutil import copyfile
from pathlib import Path
import os


def set_initial_buttoncolors():
    if int(helper.get_size()) == 1920:
        button_window_small.configure(bg="green")
    elif int(helper.get_size()) == 3840:
        button_window_big.configure(bg="green")
    if helper.is_fps_improved():
        button_window_boost.configure(bg="green")


def button_click_small():
    try:
        set_size = helper.set_size('small')
        if set_size:
            button_window_small.configure(bg="green")
            button_window_big.configure(bg="white")
            messagebox.showinfo(
                "", "Successfully changed resolution to 1920x1080!")
        else:
            messagebox.showinfo("", "Something went wrong!")
    except KeyError:
        messagebox.showinfo("", "Something went wrong, check for right path!")


def button_click_big():
    try:
        set_size = helper.set_size('big')
        if set_size:
            button_window_small.configure(bg="white")
            button_window_big.configure(bg="green")
            messagebox.showinfo(
                "", "Successfully changed resolution to 3840x1080!")
        else:
            messagebox.showinfo("", "Something went wrong!")
    except KeyError:
        messagebox.showinfo("", "Something went wrong, check for right path!")


def button_click_improvement():
    try:
        if not helper.is_fps_improved():
            helper.improve_fps()
            button_window_boost.configure(bg="green")
            messagebox.showinfo("", "Changed for better FPS!")
        else:
            button_window_boost.configure(bg="white")
    except KeyError:
        messagebox.showinfo("", "Something went wrong, check for right path!")


def button_reset():
    try:
        os.remove(path)
        os.rename(new_file, path)
        check_for_backup()
        if helper.is_fps_improved():
            button_window_boost.configure(bg="green")
        else:
            button_window_boost.configure(bg="white")
        if helper.get_size() == '1920':
            button_window_big.configure(bg="white")
            button_window_small.configure(bg="green")
        messagebox.showinfo("", "Settings have been reset")
    except KeyError:
        messagebox.showinfo("", "Something went wrong, check for right path!")


def button_start_game():
    if helper.open_game():
        messagebox.showinfo("Can't find game",
                            "RocketLeague.exe couldn't be located on the standard path. "
                            "Choose RocketLeague.exe once from Explorer. Afterwards you can start the game from here.")
        try:
            file_path = filedialog.askopenfilename()
            helper.set_path_setting('SaveFiles', 'PathToGame', file_path)
            helper.open_game()
        except KeyError:
            messagebox.showinfo(
                "", "Something went wrong, check for right path!")


def button_close():
    sys.exit(0)


def check_for_backup():
    if not Path(new_file).is_file():
        copyfile(path, new_file)


# Get path for TASystemSettings.ini
path = helper.get_path()
new_file = path[:-4] + "_default.ini"

# Check for TASystemsettings_default.ini
if not Path(path).is_file():
    messagebox.showerror("Can't find TASystemsettings.ini",
                         "Open the Game to restore the file. Close it again to modify it with this program.")
    sys.exit(0)

# Make backup copy of TASystemSettings.ini as TASystemSettings_default.ini
check_for_backup()

# Init
IMAGE_PATH = 'Source/wp_1.jpg'
WIDTH, HEIGTH = 700, 400
button_width = 15

# Initialize window
root = tk.Tk()

# Window is not resizable anymore
root.resizable(False, False)

# Set Icon for window
root.iconphoto(root, ImageTk.PhotoImage(file='Source/icon.jpg'))

# Set Title for window
root.title("Rocket League Booster - Launcher")

# Set Size of window
canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

# Set Image of canvas
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize(
    (WIDTH, HEIGTH), Image.ANTIALIAS))
# Keep a reference in case this code is put in a function.
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Add Buttons to window
# Quit Button
button_quit = Button(root, text="Quit\n", command=button_close,
                     width=button_width, bg='white')
button_quit.pack(side=RIGHT)

# Button to set resolution of Rocket League to 1920x1080
button_window_small = Button(
    root, text="1 Screen\n", command=button_click_small, width=button_width)
button_window_small.pack(side=LEFT)

# Button to set resolution of Rocket League to 3840x1080
button_window_big = Button(root, text="2 Screens\n",
                           command=button_click_big, width=button_width)
button_window_big.pack(side=LEFT)

# Set Settings in config to improve FPS
button_window_boost = Button(
    root, text="FPS Boost\n", command=button_click_improvement, width=button_width)
button_window_boost.pack(side=LEFT)

# Reset Settings in config
button_reset = Button(root, text="Reset Settings\n",
                      command=button_reset, width=button_width, bg='white')
button_reset.pack(side=LEFT)

# Reset Settings completely
button_start = Button(root, text="Start Game!\n",
                      command=button_start_game, width=button_width, bg='white')
button_start.pack(side=LEFT)

set_initial_buttoncolors()
helper.center(root)

root.mainloop()
