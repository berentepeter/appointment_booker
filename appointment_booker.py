###################################################################
#
#   https://buborekok.hu/orarend/?page=ora-osszesito&kovetkezohet=1
#
#   https://buborekok.hu/orarend/modules/mod_ajax/modal_content.php
#
#   <option value="3113">name</option>
#   
#   function onclick(event) {
#       openModal(20716)
#   }
####################################################################
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
#from selenium.webdriver.firefox.options import Options
#options = Options()
#ptions.headless = True
username = "username"
password = "password"

#driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://buborekok.hu/orarend/")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
print('Title: %s' % driver.title)

driver.find_element("name","login_email").send_keys(username)
driver.find_element("name","log_pwd").send_keys(password)
driver.find_element("name","submit").click()

driver.get("https://buborekok.hu/orarend/?page=ora-osszesito&kovetkezohet=1")
#driver.find_element("By.XPATH", "babaúszás - haladó").click()
action = ActionChains(driver)
action.move_by_offset(220, 580).click().perform()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

action.move_by_offset(950, 80).click().perform()
#action.move_by_offset(750, -85).click().perform()
action.move_by_offset(10, -380).click().perform()
Select(driver.find_element("name","child_selection")).select_by_index(0)
time.sleep(3)

driver.find_element("id","jelentkez").click()

time.sleep(3)
driver.quit()
