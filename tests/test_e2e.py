import time
import pytest
from PageObjectModel.loginPage import LoginPage
from PageObjectModel.registrationPage import RegistrationPage
from PageObjectModel.searchPage import SearchPage
from testdata.loginData import LoginData
from testdata.purchaseData import PurchaseData
from testdata.registrationData import RegistrationData
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestPurchase(BaseClass):
    # user registration
    def test_userRegistration(self,getDataRegistration):
        self.driver.implicitly_wait(5)
        global log
        log=self.get_logger()

        log.info(self.driver.title)
        log.info("User registration")

        registrationPage = RegistrationPage(self.driver)
        registrationPage.click_registerLink().click()
        registrationPage.select_gender().click()
        registrationPage.get_FirstName().send_keys(getDataRegistration["firstname"])
        registrationPage.get_LastName().send_keys(getDataRegistration["lastname"])
        registrationPage.get_birthDay().send_keys(getDataRegistration["birthday"])
        registrationPage.get_birthMonth().select_by_value(getDataRegistration["birthmonth"])
        registrationPage.get_birthYear().select_by_value(getDataRegistration["birthyear"])
        registrationPage.get_email().send_keys(getDataRegistration["email"])
        registrationPage.get_company().send_keys(getDataRegistration["company"])
        registrationPage.newsletter_Checkboc().click()
        registrationPage.get_pwd().send_keys(getDataRegistration["pwd"])
        registrationPage.get_ConfirmPwd().send_keys(getDataRegistration["confirmpwd"])
        registrationPage.click_registerButton().click()
        registration_msg=registrationPage.verify_registrationMsg().text
        assert registration_msg == "Your registration completed"
        registrationPage.click_continueBtn().click()


    # login user
    def test_userLogin(self,getDataUserLogin):


        log.info("User Login")

        loginPage=LoginPage(self.driver)
        loginPage.click_logInLink().click()
        loginPage.get_email().send_keys(getDataUserLogin["email"])
        loginPage.get_pwd().send_keys(getDataUserLogin["pwd"])
        loginPage.click_checkbox().click()
        loginPage.click_login().click()

    # purchase item
    def test_purchaseProduct(self,getDataPurchase):

        searchPage=SearchPage(self.driver)

        searchPage.search_Item().send_keys(getDataPurchase["searchItem"])
        searchedProductPage=searchPage.click_SearchBtn()
        # Object optimization


        phones = searchedProductPage.searchedProducts()
        for phone in phones:
            if phone.text == "HTC One Mini Blue":
                phone.click()
                break

        searchedProductPage.addTo_Cart().click()
        searchedProductPage.click_shoppingLink().click()
        searchedProductPage.select_checkbox().click()

        checkOutPage=searchedProductPage.click_checkoutBtn()
        # object optimization


        # self.driver.find_element(By.ID, "delete-billing-address-button").click()

        # billing
        # self.driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Keerthna")
        # self.driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("Ganeshan")
        # self.driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("keerthi123@gmail.com")

        checkOutPage.get_country().select_by_value(getDataPurchase["country"])
        checkOutPage.get_city().send_keys(getDataPurchase["city"])
        checkOutPage.get_address1().send_keys(getDataPurchase["address1"])
        checkOutPage.get_address2().send_keys(getDataPurchase["address2"])
        checkOutPage.get_zipcode().send_keys(getDataPurchase["zipcode"])
        checkOutPage.get_phNumber().send_keys(getDataPurchase["phoneNumber"])
        # explicit waits
        checkOutPage.click_addressContinueBtn().click()
        checkOutPage.click_shippingContinueBtn().click()
        checkOutPage.click_paymentContinueBtn().click()
        checkOutPage.click_paymentInfoContinueBtn().click()
        checkOutPage.click_confirmBtn().click()

        order_msg =checkOutPage.verifySuccessMsg().text
        log.info(order_msg)
        assert "successfully" in order_msg

        time.sleep(5)

    @pytest.fixture(params=RegistrationData.test_registration_data)
    def getDataRegistration(self,request):
        return request.param

    @pytest.fixture(params=LoginData.test_login_data)
    def getDataUserLogin(self,request):
        return request.param

    @pytest.fixture(params=PurchaseData.test_purchase_data)
    def getDataPurchase(self,request):
        return request.param

