import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

campo = navegador.find_element(By.XPATH, '//*[@id="login_field"]')
campo.send_keys('')
campo = navegador.find_element(By.XPATH, '//*[@id="password"]')
campo.send_keys('')
botao = navegador.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
botao.click()
sleep(2.0)

#Entra na Cisco
sleep(1.5)
navegador.execute_script("window.open('https://auth.netacad.com/auth/realms/skillsforall/protocol/openid-connect/auth?client_id=b2e-marketplace&redirect_uri=https%3A%2F%2Fwww.netacad.com%2Fdashboard&state=4f799b7a-ea49-4c86-87fe-fbaa71abf986&response_mode=fragment&response_type=code&scope=openid&nonce=ffe7d13d-18a2-44dd-8ed8-091eec87ba05&ui_locales=en-US', '_blank');")
navegador.switch_to.window(navegador.window_handles[3])

try:
    campo = WebDriverWait(navegador, 150).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    campo.send_keys('')
    campo.send_keys(Keys.ENTER)

    campo = WebDriverWait(navegador, 150).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    campo.send_keys('')
    campo.send_keys(Keys.ENTER)
except TimeoutException:
    print(f'ERRO: O Tempo de Espera foi excedido {TimeoutException}')

fechar = input("Clique Enter para fechar")