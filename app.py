import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/")
time.sleep(3)
usuario_input = driver.find_element(By.NAME,'session_key')
usuario_input.send_keys('neneiilson@gmail.com')
senha_input = driver.find_element(By.NAME,'session_password')
senha_input.send_keys('121298@Nei')
senha_input.send_keys(Keys.RETURN)
sleep(5)

driver.get("https://google.com")
time.sleep(1)

busca_input = driver.find_element(By.NAME,'q')
busca_input.send_keys('site:linkedin.com/in/ AND "Desenvolvedor" AND "kenzie academy" AND "Desenvolvedor Front-End" AND "Desenvolvedor Full Stack"')
busca_input.send_keys(Keys.RETURN)
time.sleep(5)

lista_perfil = driver.find_elements(By.XPATH,'//div[@class="yuRUbf"]/a')
lista_perfil = [perfil.get_attribute("href") for perfil in lista_perfil]

for perfil in lista_perfil:
    driver.get(perfil)
    time.sleep(2)
    try:
        time.sleep(5)
        driver.find_element(By.XPATH,'//button[normalize-space()="Conectar"]').click()
        time.sleep(2)
    except NoSuchElementException:
        pass

    try:
        time.sleep(5)
        driver.find_element(By.XPATH,'//button[normalize-space()="Enviar"]') .click()
        time.sleep(3)
    except NoSuchElementException:
        pass

driver.quit()
