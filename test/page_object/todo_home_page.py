from appium.webdriver import Remote
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy as By
from .base import BaseClass


class TodoHomePage(BaseClass):
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.btn_add_task = {"by": By.ACCESSIBILITY_ID, "locator": "Add Task"}

    def task_added_notification_shown(self) -> WebElement:
        return self.driver.find_element(
            By.ID, "com.splendapps.splendo:id/snackbar_text"
        )

    def new_task_shown(self, task_name: str) -> WebElement:
        return self.driver.find_element(
            By.XPATH,
            f'//android.widget.TextView[@resource-id="com.splendapps.splendo:id/task_name"][@text="{task_name}"]',
        )
