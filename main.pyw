import contextlib
import customtkinter as tki
from tkinter import colorchooser, PhotoImage
import keyboard as kb
import pyautogui
import os
import time as t

def start_drawing(event):
    canvas.start_x = event.x
    canvas.start_y = event.y

def continue_drawing(event):
    canvas.create_oval(event.x-current_width/2, event.y-current_width/2, event.x+current_width/2, event.y+current_width/2, fill=current_color, outline=current_color, width=current_width)
    line_width = current_width * 2 if current_width > 1 else 1
    canvas.create_line(canvas.start_x, canvas.start_y, event.x, event.y, fill=current_color, width=line_width)
    canvas.start_x = event.x
    canvas.start_y = event.y

def erase(event):
    x = event.x
    y = event.y
    items = canvas.find_overlapping(x-current_width, y-current_width, x+current_width, y+current_width)
    for item in items:
        if canvas.type(item) == 'image': continue
        canvas.delete(item)

def pick_color():
    global current_color
    color = colorchooser.askcolor(title="Pick a color")
    if color[1]:
        current_color = color[1]

def update_width(event):
    global current_width
    current_width = width_scale.get()

def close():
    """Saves drawn image and quits
    """
    toolFrame.place_configure(x=1000000,y=100000000)
    with contextlib.suppress(Exception): os.remove('bg.png')
    t.sleep(0.1)
    pyautogui.screenshot('save.png')
    root.destroy()

x,y = pyautogui.size()
root = tki.CTk(fg_color='#000001')
root.wm_attributes('-topmost',True,'-fullscreen',True, '-transparentcolor','#000001')
root.geometry(f"{x}x{y}")
root.overrideredirect(1)

kb.add_hotkey('esc',close)

canvas = tki.CTkCanvas(root,background='white',bd=0, highlightthickness=0, relief='ridge')
canvas.pack(fill=tki.BOTH, expand=True, side='bottom')

image = pyautogui.screenshot('bg.png')
img = PhotoImage(file='bg.png')
canvas.create_image(x/2,y/2,image=img)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", continue_drawing)
canvas.bind("<B3-Motion>", erase)


toolFrame = tki.CTkFrame(master=root)
toolFrame.place(x=x/3,y=0)

color_button = tki.CTkButton(toolFrame, text="Pick Color", command=pick_color)
color_button.pack(padx=5,pady=5)

width_label = tki.CTkLabel(toolFrame, text="Tool Width:")
width_label.pack(padx=5,pady=5)

width_scale = tki.CTkSlider(toolFrame, from_=1, to=50, command=update_width)
width_scale.pack(padx=5,pady=5)

current_color = "black"
current_width = 25
root.mainloop()



