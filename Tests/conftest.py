import pytest

from Pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run the tests")

@pytest.fixture
def browser(request):
    selected_browser = request.config.getoption('--browser').lower()
    if selected_browser not in ['chrome', 'firefox']:
        raise Exception('Browser nao suportado!')
    yield selected_browser


# @pytest.fixture()
# def setup(browser):
#     login_page = LoginPage(browser=browser)
#     yield  login_page
#     login_page.QuitDriver()
#
# @pytest.fixture
# def efetuar_login(setup):
#     login_page = setup
#     login_page.login()
#     yield login_page

