import pyautogui as pg
from getpass import getpass

Matricula = input("Digite sua Matricula: ")
Senha = getpass("Digite Sua Senha: ")

pg.PAUSE = 1.0

pg.press('win')
pg.write("Edge ")
pg.press('Backspace')
pg.press('enter')

pg.PAUSE = 1.5

pg.hotkey('Ctrl','t')
pg.write("https://suap.ifmt.edu.br")
pg.press('enter')
pg.write(Matricula)
pg.press('enter')
pg.write(Senha)
pg.press('enter')

pg.press('f11')
pg.hotkey('Ctrl','t')
pg.write("https://ava.cba.ifmt.edu.br/")
pg.press('enter')

pg.PAUSE = 0.5

pg.hotkey('Ctrl','Tab')
pg.hotkey('Ctrl','w')