from abc import abstractmethod


class BasePage(object):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def _validate_page(self, driver):
        return


    def search(self):
        from search import SearchRegion


