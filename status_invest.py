#
# 
# esta aplicação busca e baixa os dados de todas as açoes brasileiras a partir do site STATUSINVEST.COM
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = 'https://statusinvest.com.br/acoes/busca-avancada'

print('Fazendo requisição')
driver = webdriver.Chrome()
driver.get(URL)
sleep(2)

botao = driver.find_element(By.XPATH, "//button[@class='find waves-effect waves-light btn btn-large btn-main fw-700  fs-3 pl-2 pr-2 pl-sm-3 pr-sm-3 tooltipped']")
botao.click()
sleep(2)

download = driver.find_element(By.XPATH, "//span[@class='d-none d-sm-inline-block']")
download.click()
sleep(1)

