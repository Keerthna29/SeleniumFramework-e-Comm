from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CheckOutPage:

    country=(By.ID, "BillingNewAddress_CountryId")
    city=(By.NAME, "BillingNewAddress.City")
    address1=(By.ID, "BillingNewAddress_Address1")
    address2=(By.NAME, "BillingNewAddress.Address2")
    zipcode=(By.ID, "BillingNewAddress_ZipPostalCode")
    phoneNumber=(By.ID, "BillingNewAddress_PhoneNumber")
    address_continueBtn=(By.XPATH, "//div/button[@class='button-1 new-address-next-step-button'][1]")
    shipping_continueBtn=(By.XPATH, "//div/button[@class='button-1 shipping-method-next-step-button'][1]")
    payment_continueBtn=(By.XPATH, "//div/button[@class='button-1 payment-method-next-step-button'][1]")
    paymentInfo_continueBtn=(By.XPATH, "//div/button[@class='button-1 payment-info-next-step-button'][1]")
    confirmBtn=(By.XPATH, "//div/button[@class='button-1 confirm-order-next-step-button'][1]")
    successMsg=(By.XPATH, "//div/strong[text()='Your order has been successfully processed!']")

    def __init__(self,driver):
        self.driver=driver


    def get_country(self):
        country=Select(self.driver.find_element(*CheckOutPage.country))
        return country
    def get_city(self):
        return self.driver.find_element(*CheckOutPage.city)
    def get_address1(self):
        return self.driver.find_element(*CheckOutPage.address1)
    def get_address2(self):
        return self.driver.find_element(*CheckOutPage.address2)
    def get_zipcode(self):
        return self.driver.find_element(*CheckOutPage.zipcode)
    def get_phNumber(self):
        return self.driver.find_element(*CheckOutPage.phoneNumber)
    def click_addressContinueBtn(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.address_continueBtn)))
    def click_shippingContinueBtn(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.shipping_continueBtn)))
    def click_paymentContinueBtn(self):
        wait =  WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.payment_continueBtn)))
    def click_paymentInfoContinueBtn(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.paymentInfo_continueBtn)))
    def click_confirmBtn(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.confirmBtn)))
    def verifySuccessMsg(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(expected_conditions.visibility_of_element_located((CheckOutPage.successMsg)))