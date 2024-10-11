import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def logar(usuario, senha, campoNome, campoSenha, botao):
    if campoNome == "" and campoSenha == "" or campoNome == "" or campoSenha == "":
        campoNome = "username"
        campoSenha = "password"

    campo = navegador.find_element(By.NAME, campoNome)
    campo.send_keys(usuario)
    campo = navegador.find_element(By.NAME, campoSenha)
    campo.send_keys(senha)
    botao = navegador.find_element(By.CLASS_NAME, botao)
    botao.click()

matricula = input("Digite o numero da sua Matricula: ")
senhaAluno = getpass.getpass("Digite a sua Senha: ")

#Configura o Navegador
navegador = webdriver.Chrome()
navegador.maximize_window()

sleep(1.5)

#Entra no Suap
navegador.get("https://suap.ifmt.edu.br/accounts/login/")
logar(matricula, senhaAluno, "", "", "btn.success")
sleep(1.5)

#Entra no AVA
navegador.execute_script("window.open('https://ava.cba.ifmt.edu.br/', '_blank');")
navegador.switch_to.window(navegador.window_handles[1])
sleep(1.0)
logar(matricula, senhaAluno, "", "", "btn.btn-primary")

fechar = input("Clique Enter para fechar")