import rpa as r
import pyautogui as pg

pg.hotkey('winleft','r')
pg.write("C:\\Users\\frlc\\Desktop\\RPA.pbix")
pg.sleep(2)
pg.press('enter')
pg.sleep(18)
pg.click(x=2196, y=-208)
pg.sleep(7)
janela = pg.getActiveWindow()
janela.close()
pg.sleep(2)
pg.press('enter')



