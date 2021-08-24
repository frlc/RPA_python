import rpa as r
import pyautogui as pg
import pandas as pd

r.init(headless_mode=False)
r.url('http://rpachallenge.com/')
pg.sleep(8)
janela = pg.getActiveWindow()
janela.maximize()
r.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')
pg.sleep(2)
dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(dados, columns=['First Name',	'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])
r.click('//button[.="Start"]')

for coluna in df.itertuples():
    r.type('//input[@ng-reflect-name="labelFirstName"]', coluna[1]) 
    r.type('//input[@ng-reflect-name="labelLastName"]', coluna[2])
    r.type('//input[@ng-reflect-name="labelCompanyName"]', coluna[3])
    r.type('//input[@ng-reflect-name="labelRole"]', coluna[4])
    r.type('//input[@ng-reflect-name="labelAddress"]', coluna[5])
    r.type('//input[@ng-reflect-name="labelEmail"]', coluna[6])
    r.type('//input[@ng-reflect-name="labelPhone"]', str(coluna[7]))
    r.click('//input[@class="btn uiColorButton"]')

pg.sleep(5)
pg.screenshot('rpa_print.png')
janela.close()
