import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
from pages.register_page import RegisterPage
from common.connect_msysql import DbConnect, dbinfo
from pages.users_login_page import UsersLoginPage
from pages.users_feedbackiframe_page import UsersFeedbackiframePage


@pytest.fixture(scope="session", name="driver")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # quit是退出浏览器
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    url = "http://47.116.12.183:8200"
    return url


@pytest.fixture(scope="session")
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register


@pytest.fixture(scope="session")
def db():
    _db = DbConnect(dbinfo, "online")
    yield _db
    _db.close()


@pytest.fixture(scope="session")
def usersLoginPage(driver, base_url):
    usersLogin = UsersLoginPage(driver, base_url)
    return usersLogin


@pytest.fixture(scope="session")
def usersFeedbackPage(driver, base_url):
    feedback = UsersFeedbackiframePage(driver, base_url)
    return feedback



