from behave import given, when, then
from selene import browser
from selene.support.conditions import be

from src.main.web.screens.search_screen import SearchScreen


@given('I open Search Page')
def step_impl(context):
    SearchScreen.open()


@then('Logo should be visible')
def step_impl(context):
    SearchScreen().logoButton.should(be.visible)