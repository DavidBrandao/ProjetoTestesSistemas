import pytest

from Pages.LoginPage import LoginPage
from Pages.AccountsOverviewPage import AccountsOverviewPage

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run the tests')

@pytest.fixture
def browser(request):
    select_browser = request.config.getoption('--browser').lower()
    yield select_browser

@pytest.fixture()
def setup(browser):
    login_page = LoginPage(browser=browser)
    yield login_page
    login_page.quit_driver()

@pytest.fixture()
def log_in(setup):
    login_page = setup
    login_page.login()
    accounts_overview_page = AccountsOverviewPage(login_page.driver)
    assert accounts_overview_page.is_url_accounts_overview, 'Página incorreta!'
    yield login_page, accounts_overview_page
