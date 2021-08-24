import rpa as r
import pyautogui as pg
import pandas as pd
import os as o

r.init(headless_mode=True)
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = pg.getActiveWindow()
janela.maximize()
pg.sleep(2)

count = 1
header_value = True

while count <= 3:
    if count == 1:
        header_value = True
    else:
        header_value = False
    
    r.table('//table[@id="tableSandbox"]', 'temp.csv')
    dados = pd.read_csv('temp.csv')
    dados.to_csv(r'webtable.csv', mode='a', index=None, header=header_value)
    r.click('//a[@id="tableSandbox_next"]')
    count += 1

r.close()
csv_xls = pd.read_csv(r'webtable.csv')
csv_xls.to_excel(r'webtable.xlsx', sheet_name='webtable')
o.remove('temp.csv')
o.remove('webtable.csv')



