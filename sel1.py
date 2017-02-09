
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("http://www.google.com")

search_field = driver.find_element_by_id("lst-ib")
search_field.clear()
input_city = "san jose , CA weather"
search_field.send_keys(str(input_city))
search_field.submit()

#link1 = driver.find_element_by_link_text("The Weather Channel")
#driver.implicitly_wait(5)
#link1.click()

output = driver.find_element_by_xpath(".//*[@id='wob_wc']")
print ("Current weather forecast for the city {} ".format(input_city))
print (output.text)

#print "HI"


#first_link = driver.find_element_by_xpath('The Weather Channel').click()

#lists = driver.find_elements_by_class_name("ads-ad")

#print ("Found: " , str(len(lists)) , "searches")

#for each in lists:
 #   print each
driver.quit()



