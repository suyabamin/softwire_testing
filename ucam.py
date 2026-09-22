from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
# To Keep Browser Open Indefinitely
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# Edge Driver
service_obj = Service()
driver = webdriver.Edge(options=options, service=service_obj)

# Browser Tasks
driver.maximize_window()
driver.get("https://ucam.uiu.ac.bd/Security/LogIn.aspx")

driver.find_element(By.ID, "logMain_UserName").send_keys("0112330236")
driver.find_element(By.ID, "logMain_Password").send_keys("Sa205158@#")
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(5)
elements = driver.find_elements(By.ID, "advisor")

for E in elements:
    print(E.text)

assert "Sidratul Tanzila Tasmi" in elements[0].text
print("yes advisor is our tasmi mem")