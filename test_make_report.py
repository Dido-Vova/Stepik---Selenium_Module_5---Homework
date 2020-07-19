from selenium.webdriver.common.by import By
import time

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
REGISTRATION_TEXT = 'Thanks for registering!'
LOGIN = str(time.time()) + "@fakemail.org"
PASSWORD = "1111122222qwer"

class Locators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_FORM_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_FORM_REPEAT_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_FORM_SUBMIT_BTN = (By.NAME, 'registration_submit')
    REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div > div')

def test_user_can_see_register_success_message(browser):
    go_to_login_page(browser)
    register_new_user(browser, LOGIN, PASSWORD)
    is_message_match_expectation(browser, REGISTRATION_TEXT, \
                               *Locators.REGISTRATION_SUCCESS_MESSAGE)

def go_to_login_page(browser):
    browser.get(MAIN_PAGE_URL)
    main_page = browser.find_element(*Locators.LOGIN_LINK)
    main_page.click()

def register_new_user(browser, email, password):
    browser.find_element(*Locators.REGISTER_FORM_EMAIL_FIELD).send_keys(email)
    browser.find_element(*Locators.REGISTER_FORM_PASSWORD_FIELD).send_keys(password)
    browser.find_element(*Locators.REGISTER_FORM_REPEAT_PASSWORD_FIELD).send_keys(password)
    browser.find_element(*Locators.REGISTER_FORM_SUBMIT_BTN).click()

def is_message_match_expectation(browser, expected, how_received, what_received):
    received = browser.find_element(how_received, what_received).text.strip()
    assert expected == received, "Do not match expected and received register message"

if __name__ == '__main__':
    test_user_can_see_register_success_message()