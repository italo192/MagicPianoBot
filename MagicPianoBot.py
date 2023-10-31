# finalizar piano magico
import webbrowser
import pyautogui
from time import sleep
import keyboard
import win32api
import win32con


webbrowser.open('https://gameforge.com/en-US/littlegames/magic-piano-tiles/#')
sleep(30)
# clicar no botão
pyautogui.click(1027,424, duration=5)
sleep(60)

#iniciar o jogo
pyautogui.click(1013,383, duration=2)

# configura para clicar nas teclas

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(919,320 , (0,0,0)):
        click(919,320)
    if pyautogui.pixelMatchesColor(1004,309 , (0,0,0)):
        click(1004,309)
    if pyautogui.pixelMatchesColor(1057,321 , (0,0,0)):
        click(1057,321)
    if pyautogui.pixelMatchesColor(1133,321 , (0,0,0)):
        click(1133,321)  
