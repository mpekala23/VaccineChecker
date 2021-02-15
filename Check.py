from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client

client = Client("YOUR TWILIO ACCOUNT", "YOUR TWILIO PASSWORD")

driver = webdriver.Chrome()
driver.get('https://www.cvs.com/immunizations/covid-19-vaccine')

element = driver.find_element(By.XPATH, "//span[.='California']")

element.click()

modal = driver.find_element_by_class_name('rte-component-wraper')

lis = driver.find_elements_by_tag_name('li')

textMessage = "Eligibility:"

for li in lis:
  text = li.text
  if (len(text) > 0 and text != 'Arkansas' and text != 'California' and text != 'Massachusetts' and text != 'New Jersey'):
    textMessage += "\n" + text

client.messages.create(to="+16127038623", 
                       from_="+16144186473", 
                       body=textMessage)

driver.quit()