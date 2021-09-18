from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()


driver.get("https://fpftech.com/")
driver.find_element_by_css_selector('body > modal-container > div > div > app-lgpd-tou > div > div.modal-body > div.d-flex.justify-content-end.mt-3.mb-1 > button.btn.btn-primary').click() #concordando com o Alerta de cookies

time.sleep(2)

lista_elementos = driver.find_elements_by_class_name("course-image")
# print(item.get_attribute("alt"))

depois = False
for item in lista_elementos:
    certifica = item.get_attribute("alt")
    print(certifica)

    if (certifica == "Certificação CSM"):
        depois= certifica

if depois:  
    print("\n Encontrado a certificação: " + depois)



driver.quit