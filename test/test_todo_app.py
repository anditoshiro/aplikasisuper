import os
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import pytest

from .page_object.new_task_page import NewTaskPage
from .page_object.todo_home_page import TodoHomePage

DESIRED_CAPS = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Pixel 4a API 30",
    "automationName": "UiAutomator2",
    "app": os.path.join(os.getcwd(), "test_data", "todo_list.apk"),
}


class TestTodoListApp:
    @pytest.fixture(autouse=True)
    def setup_teardown_appium(self):
        self.appium_service = AppiumService()
        self.appium_service.start(
            args=["-a", "127.0.0.1", "-p", "4723", "-pa", "/wd/hub"]
        )
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", DESIRED_CAPS)
        self.driver.implicitly_wait(5)

        self.home_page = TodoHomePage(self.driver)
        self.task_page = NewTaskPage(self.driver)

        yield

        self.driver.close_app()
        self.appium_service.stop()

    def test_todo_create_task(self):
        task_name = "New Task"

        self.home_page.click_element(self.home_page.btn_add_task)
        self.task_page.input_text(self.task_page.input_task_name, task_name)
        self.task_page.click_element(self.task_page.input_due_date)
        self.task_page.click_element(self.task_page.btn_ok)
        self.task_page.click_element(self.task_page.input_due_time)
        self.task_page.click_element(self.task_page.btn_ok)
        self.task_page.click_element(self.task_page.input_repeat)
        self.task_page.select_repeat("Other...")
        self.task_page.click_element(self.task_page.btn_ok)
        self.task_page.click_element(self.task_page.input_add_to_list)
        self.task_page.select_list("Personal")
        self.task_page.click_element(self.task_page.btn_save_task)

        notification = self.home_page.task_added_notification_shown()
        new_task = self.home_page.new_task_shown(task_name)

        assert notification.text == "Task Added"
        assert new_task.text == task_name
