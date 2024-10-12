import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg
from time import sleep

def logar(usuario, senha, campoNome, campoSenha, botao):
    if campoNome == "" and campoSenha == "" or campoNome == "" or campoSenha == "":
        campoNome = "username"
        campoSenha = "password"

    if usuario == "" and senha == "" or usuario == "" or senha == "":
        usuario = input("Digite seu Usuario (Matricula ou Email): ")
        senha = getpass.getpass("Digite a sua Senha: ")

    campo = navegador.find_element(By.NAME, campoNome)
    campo.send_keys(usuario)
    campo = navegador.find_element(By.NAME, campoSenha)
    campo.send_keys(senha)
    botao = navegador.find_element(By.CLASS_NAME, botao)
    botao.click()

matricula = input("Digite seu usuario (Matricula ou Email): ")
senhaAluno = getpass.getpass("Digite a sua Senha: ")

#Configura o Navegador
navegador = webdriver.Chrome()
navegador.maximize_window()

sleep(1.5)

#Entra no Suap
navegador.get("https://suap.ifmt.edu.br/accounts/login/")
logar(matricula, senhaAluno, "", "", "btn.success")

#Entra no AVA
sleep(1.5)
navegador.execute_script("window.open('https://ava.cba.ifmt.edu.br/', '_blank');")
navegador.switch_to.window(navegador.window_handles[1])
sleep(1.0)
logar(matricula, senhaAluno, "", "", "btn.btn-primary")

#Entra no GitHub
sleep(1.5)
navegador.execute_script("window.open('https://github.com/login', '_blank');")
navegador.switch_to.window(navegador.window_handles[2])
sleep(2.0)



#Entra na Cisco
sleep(1.5)
navegador.execute_script("window.open('https://www.netacad.com/', '_blank');")
navegador.switch_to.window(navegador.window_handles[3])
sleep(1.5)
btLogin = navegador.find_element(By.CLASS_NAME, "btn btn--ghost.loginBtn--lfDa2")


fechar = input("Clique Enter para fechar")