import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def find_login_elements():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        submit = driver.find_element(By.ID, "login-button")

        if username and password and submit:
            print("Элементы найдены")
        else:
            print("Не все элементы найдены")
        time.sleep(5)
    finally:
        driver.quit()


find_login_elements()