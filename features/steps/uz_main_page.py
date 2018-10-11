from behave import *
import time
# from src.main.web.screens.search_screen import SearchScreen
from src.main.web_pypom.searchscreen import SearchScreen
from tests.utils.asserts import Assert


@when('User logs in via authorization form using "{email}" and "{password}"')
def step_impl(context, email, password):
    search_screen = SearchScreen().open()
    authorize_form = search_screen.authorize_form
    authorize_form.auth_form_activate.click()
    authorize_form.email_field.send_keys(email)
    authorize_form.pwd_field.send_keys(password)
    authorize_form.enter_button.click()
    # wait method for changes here
    time.sleep(1)


@then('Successful login for "{email}" and "{password}" is expected to "{pass_or_fail}"')
def step_impl(context, email, password, pass_or_fail):
    # btn_name_after = SearchScreen().authorizeForm.activateAuthorizeButton.text
    actual = SearchScreen().authorize_form.auth_form_activate.text
    expected = email.split("@")[0]
    Assert.assert_with_condition(actual == expected, pass_or_fail,
                                 message=f"Email={email} and password={password}")
# without PyPOM
# @when('User logs in via authorization form using "{email}" and "{password}"')
# def step_impl(context, email, password):
#     search_screen = SearchScreen().open()
#     authorize_form = search_screen.authorize_form
#     authorize_form.auth_form_activate.click()
#     authorize_form.email_field.send_keys(email)
#     authorize_form.pwd_field.send_keys(password)
#     authorize_form.enter_button.click()
#     # wait method for changes here
#     time.sleep(1)
#
#
# @then('Successful login for "{email}" and "{password}" is expected to "{pass_or_fail}"')
# def step_impl(context, email, password, pass_or_fail):
#     # btn_name_after = SearchScreen().authorizeForm.activateAuthorizeButton.text
#     actual = SearchScreen().authorize_form.auth_form_activate.text
#     expected = email.split("@")[0]
#     Assert.assert_with_condition(actual == expected, pass_or_fail,
#                                  message=f"Email={email} and password={password}")
