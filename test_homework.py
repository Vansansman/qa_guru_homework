from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope="session", autouse=True)
def window_size():
    browser.config.window_height = 800
    browser.config.window_width = 1200


def test_google_should_find_selene():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene'))


def test_google_should_find_selenide_negative():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should_not(have.text('User-oriented UI Python'))