from pytest import mark
from faker import Faker

fake = Faker()


class TestMyCases:
    ddt = {
        'argnames': 'name, description',
        'argvalues': [
            (fake.word(), fake.text()) for _ in range(5)
        ],
        'ids': [
            (fake.word()) for _ in range(5)
        ]
    }
    def setup(self):
        """
        :return: before test
        """
        print('hello')

    @mark.parametrize(**ddt)
    def test_new_testcase(self, desktop_app_auth, name, description):
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(name, description)
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(name)
        desktop_app_auth.test_cases.delete_test_by_name(name)

    def test_testcase_does_not_exists(self, desktop_app_auth):
        desktop_app_auth.navigate_to('Test Cases')
        assert not desktop_app_auth.test_cases.check_test_exists('sdlkfghdklsgh')

    def teardown(self):
        """
        :return: after test
        """
        print('bye')
