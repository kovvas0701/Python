import pyautogui
import webbrowser as web
from time import sleep


web.open("https://web.whatsapp.com/send?phone=++51  924 360 134")
 

sleep(10)


with open("Buenosdias.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
