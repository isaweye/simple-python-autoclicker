import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pyautogui
from pynput.keyboard import *
from sys import exit

running = True
pause = True

char = "r"
hotkey = KeyCode.from_char(char)

root = tk.Tk()
root.title("Python Autoclicker")
width=400
height=100
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

entry=tk.Entry(root)
entry["borderwidth"] = "1px"
entry["fg"] = "#333333"
entry.insert(0, "0.5")
entry.place(x=10,y=10,width=320,height=31)

typelist=["left", "right", "middle"]
listbox=ttk.Combobox(root, values=typelist)
ft = tkFont.Font(family='Times',size=10)
listbox["font"] = ft
listbox.current(0)
listbox.place(x=10,y=50,width=200,height=30)

text=tk.Label(root)
text["font"] = ft
text["fg"] = "#333333"
text["justify"] = "center"
text["text"] = f"Hotkey: "
text.place(x=250,y=50,width=111,height=30)

hotkey_entry=tk.Entry(root)
hotkey_entry["borderwidth"] = "1px"
hotkey_entry["font"] = ft
hotkey_entry["fg"] = "#333333"
hotkey_entry["justify"] = "center"
hotkey_entry.insert(0, "r")
hotkey_entry.place(x=330,y=50,width=60,height=30)

def button_cmd():
	global char, hotkey
	char = hotkey_entry.get()
	hotkey = KeyCode.from_char(char)

button=tk.Button(root)
button["bg"] = "#e9e9ed"
ft = tkFont.Font(family='Times',size=10)
button["font"] = ft
button["fg"] = "#000000"
button["justify"] = "center"
button["text"] = "SAVE"
button.place(x=332,y=10,width=60,height=30)
button["command"] = button_cmd

def on_press(key):
	global running, pause, char, hotkey

	if key == hotkey:
		if pause == True:
			pause = False
		else:
			pause = True	

lis = Listener(on_press=on_press)
lis.start()

def close():
	global running
	lis.stop()
	print("done")
	running = False
	root.quit()
	root.destroy()

root.protocol("WM_DELETE_WINDOW", close)

while running != False:
	root.update()
	if not pause:
		pyautogui.click(pyautogui.position(), button=listbox.get())
		pyautogui.PAUSE = float(entry.get())

