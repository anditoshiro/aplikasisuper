from appium.webdriver import Remote


class BaseClass:
    def __init__(self, driver: Remote) -> None:
        self.driver: Remote = driver

    def click_element(self, element_info: dict):
        self.driver.find_element(element_info["by"], element_info["locator"]).click()

    def input_text(self, element_info: dict, value: str):
        self.driver.find_element(element_info["by"], element_info["locator"]).send_keys(
            value
        )
