from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy as By
from .base import BaseClass


class NewTaskPage(BaseClass):
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.input_task_name = {
            "by": By.ID,
            "locator": "com.splendapps.splendo:id/edtTaskName",
        }
        self.input_due_date = {
            "by": By.ID,
            "locator": "com.splendapps.splendo:id/edtDueD",
        }
        self.btn_ok = {"by": By.ID, "locator": "android:id/button1"}
        self.input_due_time = {
            "by": By.ID,
            "locator": "com.splendapps.splendo:id/edtDueT",
        }
        self.input_repeat = {
            "by": By.ID,
            "locator": "com.splendapps.splendo:id/spinnerRepeat",
        }
        self.input_add_to_list = {
            "by": By.ID,
            "locator": "com.splendapps.splendo:id/spinnerLists",
        }
        self.btn_save_task = {"by": By.ACCESSIBILITY_ID, "locator": "Save Task"}

    def select_repeat(self, repeat_options: str):
        self.driver.find_element(
            By.XPATH, f'//android.widget.TextView[@text="{repeat_options}"]'
        ).click()

    def select_list(self, list_options: str):
        self.driver.find_element(
            By.XPATH, f'//android.widget.TextView[@text="{list_options}"]'
        ).click()
