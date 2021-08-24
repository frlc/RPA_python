import rpa as r
import pyautogui as pg
import cv2

pg.doubleClick(1404, -275)
pg.sleep(4)
pg.write('https://www.udemy.com/')
pg.press('enter')
janela = pg.getActiveWindow()
janela.maximize()
pg.sleep(4)

item_pesquisa = pg.locateOnScreen('C:\\Users\\frlc\\Documents\\RPA\\imagens\\Pesquisa.PNG', confidence=0.8)
centro_imagem = pg.center(item_pesquisa)
xPesquisa, yPesquisa = centro_imagem

pg.moveTo(xPesquisa, yPesquisa, duration=1)
pg.click(xPesquisa, yPesquisa)
pg.sleep(1)
pg.write('fernando cruz')
pg.press('enter')
pg.sleep(3)
pg.screenshot('C:\\Users\\frlc\\Documents\\RPA\\imagens\\cursos_1.png')
pg.sleep(2)
janela.close()