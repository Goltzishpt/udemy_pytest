import logging

from playwright.sync_api import Browser
from playwright.sync_api import Request, Route, ConsoleMessage, Dialog
from page_objects.test_cases import TestCases
from page_objects.demo_pages import DemoPages


class App:
    def __init__(self, browser: Browser,
                 base_url: str,
                 **kwargs):

        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)
        self.demo_pages = DemoPages(self.page)

        def console_handler(message: ConsoleMessage) -> None:
            if message.type == 'error':
                logging.error(f'{self.page.url}')

        self.page.on('console', console_handler)

        def dialog_handler(dialog: Dialog)  -> None:
            logging.warning(f'page: {self.page.url}, '
                            f'dialog text: {dialog.message}')
            dialog.accept()

        self.page.on('dialog', dialog_handler)

    def goto(self, endpoint: str, use_base_url=True) -> None:
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def navigate_to(self, menu: str) -> None:
        self.page.click(f'css=header >> text="{menu}"')
        self.page.wait_for_load_state()

    def login(self, login: str, password: str) -> None:
        self.page.get_by_label("Username:").fill(login)
        self.page.get_by_label("Password:").fill(password)
        self.page.get_by_label("Password:").press("Enter")

    def create_test(self, test_name: str, test_description: str) -> None:
        self.page.locator("#id_name").fill(test_name)
        self.page.get_by_label("Test description").fill(test_description)
        self.page.get_by_role("button", name="Create").click()

    def click_menu_button(self) -> None:
        self.page.wait_for_load_state()
        return self.page.click('.menuBtn')

    def is_menu_button_visible(self) -> bool:
        self.page.wait_for_load_state()
        return self.page.is_visible('.menuBtn')

    def get_location(self) -> None:
        self.page.wait_for_load_state()
        return self.page.text_content('.position')

    def intercept_requests(self, url: str, payload: str) -> None:
        def handler(route: Route, request: Request):
            route.fulfill(status=200, body=payload)

        self.page.route(url, handler)

    def stop_intercept(self, url: str) -> None:
        self.page.unroute(url)

    def refresh_dashboard(self) -> None:
        self.page.click('input')

    def get_total_tests_stats(self) -> None:
        self.page.wait_for_selector('.total >> span')
        return self.page.text_content('.total >> span')

    def close(self) -> None:
        self.page.close()
        self.context.close()

