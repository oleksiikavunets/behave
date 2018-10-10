from behave import given, then
from selene import browser
from selene.support.conditions import be

from src.main.web.screens.search_screen import SearchScreen


@given('I open Search Page')
def step_impl(context):
    SearchScreen.open()


@then('Logo should be visible')
def step_impl(context):
    SearchScreen().logoButton.should(be.visible)


@then('Page title should be "{title}"')
def step_impl(context, title):
    title_actual = browser.title()
    assert title_actual == title, "Search screen has wrong title!! \nExpected title -> " + title + "\nActual title -> " + title_actual
