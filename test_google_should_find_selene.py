import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope="session", autouse=True)
def windows_size():
    browser.config.window_height = 600
    browser.config.window_width = 1000

def test_google_should_find_seen():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene'))

def test_google_should_find_seen_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene-UI'))




