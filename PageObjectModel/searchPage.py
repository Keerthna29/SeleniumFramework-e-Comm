from selenium.webdriver.common.by import By

from PageObjectModel.searchedProductPage import SearchedProductPage


class SearchPage:
    searchItem=(By.ID, "small-searchterms")
    searchBtn=(By.XPATH, "//form/button[text()='Search']")

    def __init__(self,driver):
        self.driver=driver


    def search_Item(self):
        return self.driver.find_element(*SearchPage.searchItem)
    def click_SearchBtn(self):
        self.driver.find_element(*SearchPage.searchBtn).click()
        searchedProductPage=SearchedProductPage(self.driver)
        return searchedProductPage
    # Object optimization