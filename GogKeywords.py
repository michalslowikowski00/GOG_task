from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GogKeywords:
    def __init__(self):
        pass

    def check_url(self):
        """Method will check if current URL -- robot framework will do assertion."""

        test_url = self.driver.current_url
        return test_url

    def find_all_in_genre(self):
        """Method will iterate every element in Genre web element.
        Click on it and check current url after every iteration."""

        list_game_types = ["Role-playing", "Simulation", "Indie", "Racing", "Sports",
                           "Action", "Strategy", "Shooter", "Adventure"]
        try:
            for i in range(len(list_game_types)):
                xpath = "//span[@ng-bind-html='::choice.title' and contains(text(), '{0}')]".format(list_game_types[i])
                print xpath
                game_type = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                game_type.click()
                self.select_element()
                self.select_genre()

                for ii in range(len(list_game_types)):
                    url = "https://www.gog.com/games/{0}?sort=bestselling&page=1".format(list_game_types[i]).lower()
                    assert url in self.driver.current_url
                continue
        except StaleElementReferenceException as e:
            raise e

    def init_driver(self):
        """Setup option for Chrome web browser which allows expand window browser"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(1250, 700)

    def select_element(self):
        """Method will check if after selecting role-playing type of game X mark will be
        visible next to tag Genre."""

        element_to_mark_in_category = self.driver.find_element_by_css_selector(
            "div[hook-test='category'] > i[ng-show='filter.isSelected()']")
        return element_to_mark_in_category

    def select_genre(self):
        """Method will find web element Genre and click on it."""

        element_genre = self.driver.find_element_by_css_selector(
            "div[hook-test='category'].filter._dropdown.filter--category.is-contracted")
        element_genre.click()

    def set_up_browser(self):
        """Webdriver will open https://www.gog.com/games?sort=bestselling&page=1"""
        self.init_driver()
        self.driver.get("https://www.gog.com/games?sort=bestselling&page=1")

    def tear_down(self):
        self.driver.close()
        
