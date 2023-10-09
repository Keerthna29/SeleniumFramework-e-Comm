from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationPage:
    register_link=(By.LINK_TEXT, "Register")
    gender=(By.ID, "gender-female")
    first_name=(By.ID, "FirstName")
    last_name=(By.ID, "LastName")
    birth_day=(By.NAME, "DateOfBirthDay")
    birth_month=(By.NAME, "DateOfBirthMonth")
    birth_year=(By.NAME, "DateOfBirthYear")
    email=(By.ID, "Email")
    company=(By.CSS_SELECTOR, "#Company")
    newsletter_ch=(By.ID, "Newsletter")
    password=(By.ID, "Password")
    confirm_pwd=(By.ID, "ConfirmPassword")
    register_btn=(By.CSS_SELECTOR, "button[id='register-button']")
    registration_msg=(By.CSS_SELECTOR, "div[class='result']")
    continue_btn=(By.XPATH, "//a[text()='Continue']")

    def __init__(self,driver):
        self.driver=driver


    def click_registerLink(self):
        return self.driver.find_element(*RegistrationPage.register_link)
    def select_gender(self):
        return self.driver.find_element(*RegistrationPage.gender)
    def get_FirstName(self):
        return self.driver.find_element(*RegistrationPage.first_name)
    def get_LastName(self):
        return self.driver.find_element(*RegistrationPage.last_name)
    def get_birthDay(self):
        return self.driver.find_element(*RegistrationPage.birth_day)
    def get_birthMonth(self):
        month=Select(self.driver.find_element(*RegistrationPage.birth_month))
        return month


    def get_birthYear(self):
        year=Select(self.driver.find_element(*RegistrationPage.birth_year))
        return year

    def get_email(self):
        return self.driver.find_element(*RegistrationPage.email)
    def get_company(self):
        return self.driver.find_element(*RegistrationPage.company)
    def newsletter_Checkboc(self):
        return self.driver.find_element(*RegistrationPage.newsletter_ch)
    def get_pwd(self):
        return self.driver.find_element(*RegistrationPage.password)
    def get_ConfirmPwd(self):
        return self.driver.find_element(*RegistrationPage.confirm_pwd)
    def click_registerButton(self):
        return self.driver.find_element(*RegistrationPage.register_btn)
    def verify_registrationMsg(self):
        return self.driver.find_element(*RegistrationPage.registration_msg)
    def click_continueBtn(self):
        return self.driver.find_element(*RegistrationPage.continue_btn)





