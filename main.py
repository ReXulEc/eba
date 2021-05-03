from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


with open('Şifre/username.txt', 'r') as file:
	username = file.read().replace('\n', '')

with open('Şifre/password.txt', 'r') as file:
	password = file.read().replace('\n', '')

url = "https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp"

print('--------------------------------------------------------------')
print('         Uygulamayı Kullandığınız İçin Teşekkürler!')
print('Bu Uygulamayı Kullanarak Yasal Şartları Kabul Etmiş Olursunuz.')
print('                   ReXulEc // rexulec.com')
print('--------------------------------------------------------------')
sleep(3)

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"Driver\chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get(url)

driver.find_element_by_name("tckn").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector(".nl-form-send-btn").click()

sleep(2)

while True:
	element = WebDriverWait(driver, 10).until(
	    EC.element_to_be_clickable((By.ID, "joinMeeting"))
	)

	driver.find_element_by_id("joinMeeting").click()
	
	print("Başarılı")


print("Made with python <3 // ReXulEc")

