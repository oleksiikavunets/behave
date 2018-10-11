from behave import given, then
from selene import browser

# from src.main.web.screens.search_screen import SearchScreen
from src.main.web_pypom.searchscreen import SearchScreen


@given('User opens Search Page')
def step_impl(context):
    SearchScreen().open()


@then('Logo should be visible')
def step_impl(context):
    assert SearchScreen().open().logo_button.is_displayed() is True


@then('Page title should be "{title}"')
def step_impl(context, title):
    title_actual = browser.title()
    assert title_actual == title, "Search screen has wrong title!! \nExpected title -> " + title + "\nActual title -> " + title_actual

# without PyPOM
# @given('User opens Search Page')
# def step_impl(context):
#     SearchScreen().open()
#
#
# @then('Logo should be visible')
# def step_impl(context):
#     assert SearchScreen().open().logo_button.is_displayed() is True
