import math
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

import time

browser = webdriver.Chrome()
try:

    browser.implicitly_wait(5)
    browser.get("https://coffeecuattro.ru/")

    
    #Регистрация нового аккаунта

    # print("Регистрация нового аккаунта", end='')
    # browser.find_element(By.CLASS_NAME,"top-panel-div-span").click()
    # browser.find_element(By.LINK_TEXT, "Регистрация учетной записи").click()  
    # browser.find_element(By.ID, "register_firstname").send_keys("testo121") 
    # time.sleep(1)
    # browser.find_element(By.ID, "register_lastname").send_keys("testova121") 
    # time.sleep(1)
    # browser.find_element(By.ID, "register_telephone").send_keys("+7911200122")
    # time.sleep(1)
    # browser.find_element(By.ID, "register_email").send_keys("testo125@gmail.com")
    # time.sleep(1)
    # browser.find_element(By.ID, "register_password").send_keys("testo")
    # time.sleep(1)
    # browser.find_element(By.ID, "register_postcode").send_keys("192322")    
    # time.sleep(1)
    # browser.find_element(By.ID, "register_address_1").send_keys("улица пушкина дом 23 к3 квартира 9")  
    # time.sleep(1)
    # browser.find_element(By.ID, "simpleregister_button_confirm").click()
    # time.sleep(1)
    # browser.find_element(By.LINK_TEXT, "ПРОДОЛЖИТЬ").click()
    # assert browser.find_element(By.CSS_SELECTOR,"#content > h1").text == "Личный кабинет"
    # print(" - успешно")
    
    #  Вход и Выход из аккаунта
    print("Вход в аккаунт", end='')
    browser.find_element(By.ID,"modaltrigger").click()
    time.sleep(1)
    browser.find_element(By.ID,"email").send_keys("testo@gmail.com") 
    time.sleep(1)
    browser.find_element(By.ID,"password").send_keys("test")  
    time.sleep(1)
    browser.find_element(By.NAME,"loginbtn").click()
    time.sleep(1)
   
    print(" - успешно")

    # print("Выход из аккаунта", end='')
    # time.sleep(1)
    # browser.delete_all_cookies()
    # time.sleep(1)
    # browser.get("https://coffeecuattro.ru/") 
    # time.sleep(1)
    # assert browser.find_element(By.LINK_TEXT, "мой аккаунт").text == "мой аккаунт"
    # print(" - успешно")
    # time.sleep(10)

    
    
#search-column > span > button

    # #Добавление товара в корзину и проверка наличия его там
    print("Добавление товара в корзину и проверка наличия его там", end='') 
    browser.find_element(By.LINK_TEXT,"КОФЕ").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,"form-control.input-lg").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,"form-control.input-lg").send_keys("кофе в зернах cuattro espresso blend")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,"#search-column > span > button").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,"#content > div.product-grid.row > div:nth-child(1) > div > div.product-about > div.product-buttons > a").click()
    time.sleep(1)
    assert browser.find_element(By.CLASS_NAME,"alert.alert-success").text == " Товар Кофе в зернах CUATTRO Espresso Blend добавлен в корзину покупок!" 
    print(" - успешно")


    time.sleep(5)
finally:
    browser.quit()