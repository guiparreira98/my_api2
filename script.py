from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o navegador
driver = webdriver.Chrome()
driver.get("https://www.ideep.tech/app/")

try:
    wait = WebDriverWait(driver, 5)

    # Fazer login
    campo_email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    campo_email.send_keys("zhang.ling@ceodofuturo.org")

    campo_senha = wait.until(EC.element_to_be_clickable((By.ID, "senha")))
    campo_senha.send_keys("2023")

    botao_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    botao_login.click()

    # Esperar o carregamento do dashboard
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'dashboard')]")))

    # Clicar em "Relatórios"
    link_relatorios = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[2]/div[1]/div[1]/div/div/h3/a')))
    link_relatorios.click()

except Exception as e:
    print(f"Erro: {e}")

finally:
    driver.quit()
