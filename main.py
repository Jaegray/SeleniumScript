from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Safari  # browser drive

driver = Safari()  # creating an instance of Safari browser
driver.get("https://www.ziprecruiter.com/Salaries/Cloud-Engineer-Salary")
assert "Salary" in driver.title  # pulling title

