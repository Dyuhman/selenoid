from selenium import webdriver
import time

capabilities = {
    "browserName": "chrome",
    "browserVersion": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}



link = "http://suninjuly.github.io/find_xpath_form"

try:
#    browser = webdriver.Chrome()
    browser = webdriver.Remote(
        command_executor="http://10.214.1.247:4444/wd/hub",
        desired_capabilities=capabilities)
    
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_xpath("/html/body/div/form/div/button[text() = \"Submit\"]")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
