from selenium.webdriver.common.by import By

from PageObjectModel.checkoutPage import CheckOutPage


class SearchedProductPage:
    searched_products=(By.XPATH, "//div/h2")
    addToCart=(By.ID, "add-to-cart-button-19")
    shopping_link=(By.XPATH, "//a/span[text()='Shopping cart']")
    checkbox=(By.XPATH, "//div/input[@type='checkbox']")
    checkoutBtn=(By.CSS_SELECTOR, "#checkout")

    def __init__(self,driver):
        self.driver=driver


    def searchedProducts(self):
        return self.driver.find_elements(*SearchedProductPage.searched_products)
    def addTo_Cart(self):
        return self.driver.find_element(*SearchedProductPage.addToCart)
    def click_shoppingLink(self):
        return self.driver.find_element(*SearchedProductPage.shopping_link)
    def select_checkbox(self):
        return self.driver.find_element(*SearchedProductPage.checkbox)
    def click_checkoutBtn(self):
        self.driver.find_element(*SearchedProductPage.checkoutBtn).click()
        checkOutPage=CheckOutPage(self.driver)
        return checkOutPage
    # object optimization