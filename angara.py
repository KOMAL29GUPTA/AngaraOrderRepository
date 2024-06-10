import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.angara.in/")

driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='ecomsend__Modal__CloseButton _closeBtn_4tu8s_236']").click()
driver.find_element(By.CSS_SELECTOR,"a[data-wau-slideout-target='searchbox']").click()
driver.find_element(By.XPATH,"//input[@title='Search our store']").click()
# Pass the value in the Search field.
driver.find_element(By.ID,"gl-d-searchbox-input").send_keys("pendant")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"View all products").click()
# Click on a particular product.
driver.find_element(By.XPATH,"//div[@class='spf-product-card__inner']").click()
driver.find_element(By.ID,"add-to-card-btn").click()
time.sleep(5)
driver.find_element(By.ID,"checkout").click()
# Fill the contact or shipping address form.
driver.find_element(By.XPATH,"//input[@placeholder='Email or mobile phone number']").send_keys("test@gmail.com")
driver.find_element(By.ID,"TextField0").send_keys("Komal")
driver.find_element(By.CSS_SELECTOR,"input[name='lastName']").send_keys("Gupta")
driver.find_element(By.XPATH,"//input[@placeholder='Address']").send_keys("Sector 50 Noida")
driver.find_element(By.CSS_SELECTOR,"input[name='city']").send_keys("Noida")
driver.find_element(By.CSS_SELECTOR,"select[name='zone']").send_keys("uttar pradesh")
driver.find_element(By.CSS_SELECTOR,"input[name='postalCode']").send_keys("201301")
driver.find_element(By.CSS_SELECTOR,"input[type='tel']").clear()
driver.find_element(By.CSS_SELECTOR,"input[type='tel']").send_keys("9876543218")
time.sleep(5)
# Scroll the page before clicking on the Submit button.
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
time.sleep(2)
# Click on the redio button to select the COD payment method.
radioButtons = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
radioButtons[1].click()
assert radioButtons[1].is_selected()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
# Click on the 'Complete order CTA.
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.close()
