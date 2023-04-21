import json
import logging
import os
import pytest
from settings import *
from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App
from settings import BASE_URL, USER, DEVICE, BROWSER_OPTIONS


@fixture(autouse=True, scope='session')
def precondition():
    logging.info('setup precondition state')
    yield
    logging.info('setup postcondition state')


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(
    scope='session',
    params=['chromium', 'firefox', 'webkit'],
    ids=['chromium', 'firefox', 'webkit']
)
def get_browser(get_playwright, request):
    browser = request.param
    os.environ['PWBROWSER'] = browser
    headless = request.config.getini('headless')
    if headless == 'True':
        headless = True
    else:
        headless = False

    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        bro = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'
    yield bro
    bro.close()
    del os.environ['PWBROWSER']


@fixture(scope='class')
def desktop_app(get_browser):
    # base_url = request.config.getoption('--base_url')
    # base_url = request.config.getini('base_url')
    app = App(
        get_browser,
        base_url=BASE_URL,
        **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='class')
def desktop_app_auth(desktop_app):
    desktop_app.goto('/login')
    desktop_app.login(**USER)
    yield desktop_app


@fixture(scope='class', params=['Iphone 12 Pro', 'Pixel 5'])
def mobile_app(get_playwright, get_browser, request):
    if os.environ.get('PWBROWSER') == 'firefox':
        pytest.skip()
    device = request.param
    device_config = get_playwright.devices.get(device)
    if device_config is not None:
        device_config.update(BROWSER_OPTIONS)
    else:
        device_config = BROWSER_OPTIONS
    app = App(
        get_browser,
        base_url=BASE_URL,
        **device_config)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='class')
def mobile_app_auth(mobile_app):
    mobile_app.goto('/login')
    mobile_app.login(**USER)
    yield mobile_app


def pytest_addoption(parser):
    # parser.addoption('--secure', action='store', default='secure.json')
    parser.addoption('--base_url', action='store', default=BASE_URL)
    parser.addoption('--device', action='store', default='')
    parser.addoption('--browser', action='store', default='chromium')
    parser.addini(
        'headless',
        help='run browser of site in headless mode',
        default=True
    )
    # parser.addini(
    #     'base_url',
    #     help='base url of site under test',
    #     default=BASE_URL
    # )


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())
