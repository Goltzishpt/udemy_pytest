from playwright.sync_api import Page


class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def check_test_exists(self, test_name:str) -> bool:
        return self.page.query_selector(f'css=tr >> text="{test_name}"') is not None

    def delete_test_by_name(self, test_name) -> None:
        row = self.page.query_selector(f'*css=tr >> text="{test_name}"')
        row.query_selector('.deleteBtn').click()

    def check_columns_hidden(self) -> bool:
        description = self.page.is_hidden('.thDes')
        author = self.page.is_hidden('.thAuthor')
        executor = self.page.is_hidden('.thLast')
        return description and author and executor
