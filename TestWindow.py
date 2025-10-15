import tkinter as tk
import threading
import time

numtocountto = None

window = tk.Tk()
window.title("Count")
window.geometry("400x320")
window.resizable(False,False)

label = tk.Label(text="Enter Number to count to",height=2,width=50)
label.pack()

text_box = tk.Text(width=30,height=7)
text_box.pack()

def buttonpressed(event):
    global numtocountto
    numtocountto = int(text_box.get("1.0",tk.END))

    window.destroy()

button = tk.Button(text="Enter",relief="raised")
button.bind("<Button-1>",buttonpressed)
button.pack()

window.mainloop()

DisplayWindow = tk.Tk()
DisplayWindow.title("Now it counts")
DisplayWindow.geometry("400x150")
DisplayWindow.resizable(False,False)

DisplayNum = tk.Label(DisplayWindow,text=f'Click to count to: {numtocountto}')
DisplayNum.pack()

DisplayText = tk.Label(DisplayWindow,height=5,width=30,font=("Arial",25),text=0)
DisplayText.pack()

def count():
    for currentnum in range(numtocountto):
        time.sleep(0.5)
        currentnum += 1
        DisplayText.config(text=currentnum)

def Connection(event):
    DisplayWindow.unbind('<Button-1>')
    countthread = threading.Thread(target=count)
    countthread.start()

DisplayWindow.bind('<Button-1>',Connection)

DisplayWindow.mainloop()
