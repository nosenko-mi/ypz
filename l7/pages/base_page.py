from abc import abstractmethod


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        self._validate_page(driver)

    def _validate_page(self, driver):
        return

    def fill_field(self, locator, data):
        try:
            self.driver.find_element(locator[0], locator[1]).send_keys(data)
        except Exception as e:
            print(e)

    def click_button(self, locator):
        try:
            self.driver.find_element(locator[0], locator[1]).submit()
        except Exception as e:
            print(e)

    def search(self, locator, data):
        try:
            self.driver.find_element(locator[0], locator[1]).send_keys(data).submit()
        except Exception as e:
            print(e)


    class InvalidPageException(Exception):
        pass

    class ElementIsMissingException(Exception):
        pass
