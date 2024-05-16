import time
import pyautogui
import pandas as pd
time.sleep(5)
pyautogui.PAUSE= 0.5
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
time.sleep(10)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')  
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')                
time.sleep(10)
pyautogui.click(x=758, y=367)
pyautogui.write('gab@gmail.com')
pyautogui.press('tab')
pyautogui.write('gab123')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=864, y=366)
tabela = pd.read_csv('produtos.csv')
for linha in tabela.index:
    pyautogui.click(x=622, y=261)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    
    





