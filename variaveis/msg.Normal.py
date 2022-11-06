import pyttsx3
engine = pyttsx3.init()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


def msgWpp():
    wichPerson = input('qual pessoa voce deseja mandar mensagem?')
    txt = input('qual mensagem voce quer enviar?')
    if wichPerson == '':
        pass
    else:
        nav = webdriver.Chrome()
        pyautogui.hotkey('win')
        time.sleep(2)
        pyautogui.write('google')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('https://web.whatsapp.com/')
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(11)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.write(f'{wichPerson}')
        time.sleep(2)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        pyautogui.write(f'{txt}')
        pyautogui.hotkey('enter')



msgWpp()
