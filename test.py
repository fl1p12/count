import pyautogui
import time
import keyboard

num_goal = 50

time.sleep(5)

for i in range(num_goal):
    pyautogui.write(str(i+1))
    pyautogui.press("backspace",len(str(i+1)))
    if keyboard.is_pressed("x"):
        print("broke")
        break
