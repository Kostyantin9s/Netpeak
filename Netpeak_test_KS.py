# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def main():
    browser_service = Service('D:\driver\chromedriver.exe')
    browser = webdriver.Chrome(service=browser_service)
    browser.implicitly_wait(10)
    #bugfix next line
    browser.maximize_window()

    '''1'''
    browser.get('https://netpeak.ua/')
    print("1: go to netpeak.ua ok")
    time.sleep(4)

    '''2'''
    button_about_us = browser.find_element(By.XPATH, "//*[contains(text(), 'О нас')]")
    button_about_us.click()
    time.sleep(4)
    button_teams = browser.find_element(By.XPATH, "//*[contains(text(), 'Команда')]")
    button_teams.click()

    print("2: click buttons about us and teams ok")
    time.sleep(4)

    '''3'''

    button_join = browser.find_element(By.XPATH, "//*[contains(text(), 'Стать частью команды')]")
    button_join.click()

    browser.switch_to.window(browser.window_handles[len(browser.window_handles) - 1])
    if 'Работа в Netpeak' not in browser.title:
        raise Exception('3: Bad title! Title not contains text \'Работа в Netpeak\' current title ', browser.title)
    else:
        print("3: go to work to netpeak and check page ok")
    time.sleep(4)

    '''4'''

    button_wont_to_work = browser.find_element(By.XPATH, "//*[contains(text(), 'Я хочу работать в Netpeak')]")

    if not button_wont_to_work.is_enabled() or not button_wont_to_work.is_displayed():
        raise Exception('4: Button Я хочу работать в Netpeak is not clickable')
    else:
        print("4: all ok target button is clickable")
    time.sleep(4)

    '''5'''
    browser.switch_to.window(browser.window_handles[len(browser.window_handles) - 2])

    button_user_office = browser.find_element(By.XPATH, "//*[contains(text(), 'Личный кабинет')]")
    button_user_office.click()
    print("5: button user office click ok")
    time.sleep(4)

    '''6'''
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))  # внутри ренжа кол-во символов
    browser.switch_to.window(browser.window_handles[len(browser.window_handles) - 1])

    login_input = browser.find_element(By.ID, 'login')
    login_input.send_keys(random_string)

    password_input = browser.find_element(By.ID, 'password')
    password_input.send_keys(random_string)

    print("6: write random string to login and pass fields ok")
    time.sleep(4)

    '''7'''

    login_button = browser.find_element(By.CSS_SELECTOR, 'button.enter')

    if login_button.is_enabled():
        raise Exception('7: login button is active')
    else:
        print('7: login button is disabled all ok')
    time.sleep(4)

    '''8'''

    gdpr_checkbox = browser.find_element(By.CSS_SELECTOR, 'md-checkbox.gdpr')
    gdpr_checkbox.click()
    print("8: gdpr checkbox click ok")
    time.sleep(4)

    '''9'''
    login_button.click()
    invalid_creds_toast = browser.find_element(By.CSS_SELECTOR, 'span.md-toast-text')
    if invalid_creds_toast.text == 'Неправильный логин или пароль':
        print('9: invalid login toast ok')
    else:
        raise Exception('9: invalid login toast fail')
    time.sleep(4)

    '''10'''

    login_input = browser.find_element(By.ID, 'login')
    password_input = browser.find_element(By.ID, 'password')

    if login_input.value_of_css_property(
            'border-bottom-color') == 'rgba(221, 44, 0, 1)' and password_input.value_of_css_property(
            'border-bottom-color') == 'rgba(221, 44, 0, 1)':
        print("10: login and password input as red all ok")
    else:
        raise Exception('10: login and password input as red fail')
    time.sleep(4)

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print("Start test")
        main()
        print("Finish test")
        print("All ok")
    except Exception as e:
        print("Test failed with reason :", e)