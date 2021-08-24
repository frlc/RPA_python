import pyautogui as pg

def Robot01():
    print(1/0)
    pg.FAILSAFE = False
    pg.hotkey('win', 'r')
    pg.typewrite('notepad', 0.5)
    pg.press('enter')
    pg.sleep(2)
    pg.typewrite('Hello world!', 0.5)
    pg.sleep(2)
    janela = pg.getActiveWindow()
    janela.close()
    pg.press('right')
    pg.sleep(2)
    pg.press('enter')
