import rpa as r
import pyautogui as pg

r.init()
r.url('https://www.google.com')
janela = pg.getActiveWindow()
janela.maximize()
r.wait(2)
r.type('input[name="q"]', 'RPA[enter]')
r.wait(2)
r.snap('page', 'rpa_print.png')
r.wait(2)
r.close()
