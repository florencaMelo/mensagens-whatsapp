#0 vai perg o que eu quero fazer com o reconhecimento de voz
import pyttsx3
engine = pyttsx3.init()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pywhatkit

def Inicio():
    engine.say('olá, o que você deseja?')
    engine.runAndWait()
    escolhas = int(input('''
    [1] = enviar uma mensagem agora para alguém 
    [2] = agendar ou criar uma mensagem automática'''
    ))
    
    if escolhas == 1:
        msgWpp()

    if escolhas == 2:
        msgAutomatica()



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


def msgAutomatica():
    changeOrDo = int(input(
    '''digite:
    [1] = se voce deseja agendar uma mensagem automatica
    [2] = se voce deseja mandar uma mensagem automatica já existente'''
    ))

    if changeOrDo == 1:
        askArk = input('deseja consultar o banco de dados das mensagens já existentes?')
        if askArk == 'sim':
            with open('salvos.txt', 'r') as ark:
                msg = ark.readlines()
            print(msg)
        
        else:
            agendamento = input(print('''
            edite no seu código o agendamento da mensagem e responda "pronto" ao acabar.
            segue o modelo de alteração:
            pywhatkit.sendwhatmsg(numero de telefone, 'mensagem', horas, minutos)
            '''))

            if agendamento == 'pronto':
                pywhatkit.sendwhatmsg('+5534997780017', 'oi', 23, 8)


    if changeOrDo == 2:
        msgsFeitas()
    

def msgsFeitas ():
    escolhasMsg = int(input(
    ''' escolha uma das opções salvas para o envio de mensagem automático
    [1] = bom dia mãe
    [2] = oi @
    '''))

    if escolhasMsg == 1:
        pywhatkit.sendwhatmsg('+5534999479717', 'bom dia mamae', 6, 40)

    if escolhasMsg == 2:
        pywhatkit.sendwhatmsg('+5534997780017', 'oi gatinho me acorda', 6, 30)


Inicio()


