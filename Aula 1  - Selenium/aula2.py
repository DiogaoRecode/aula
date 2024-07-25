from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

browser = Firefox()

link = 'https://google.com'

browser.get(link)

input_area = browser.find_element(By.NAME,"q")

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)
sleep(3)
result_search = browser.find_elements(By.TAG_NAME, 'h3')
print(result_search)

for result in result_search:
    if result.text == 'Instituto Joga Junto' and result.text is not None:  
      result.click()
      print("FOIII!")
      break

browser.find_element(By.ID, "nome").send_keys("Diogo Reis")
browser.find_element(By.ID, "email").send_keys("diogoeng.mobilidade@gmail.com")
input_assunto = browser.find_element(By.ID, "assunto")
select = Select(input_assunto)
select.select_by_visible_text("Ser facilitador")
browser.find_element(By.ID, "mensagem").send_keys("Aspirantes da Automaçao")

button_enviar = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")
button_enviar.submit()