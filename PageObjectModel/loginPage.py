from selenium.webdriver.common.by import By


class LoginPage:
    login_link=(By.LINK_TEXT, "Log in")
    email=(By.ID, "Email")
    pwd=(By.ID, "Password")
    rememberMe_ch=(By.NAME, "RememberMe")
    submitBtn=(By.XPATH, "//div/button[@type='submit']")

    def __init__(self,driver):
        self.driver=driver

    def click_logInLink(self):
        return self.driver.find_element(*LoginPage.login_link)

    def get_email(self):
        return self.driver.find_element(*LoginPage.email)
    def get_pwd(self):
        return self.driver.find_element(*LoginPage.pwd)
    def click_checkbox(self):
        return self.driver.find_element(*LoginPage.rememberMe_ch)
    def click_login(self):
        return self.driver.find_element(*LoginPage.submitBtn)