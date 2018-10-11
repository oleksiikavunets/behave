from behave import *
import time
from src.main.web.screens.search_screen import SearchScreen
from tests.utils.asserts import Assert


@when('User logs in via authorization form using "{email}" and "{password}"')
def step_impl(context, email, password):
    authorize_form = SearchScreen().authorizeForm
    authorize_form.activateAuthorizeButton.click()
    authorize_form.emailField.send_keys(email)
    authorize_form.passwordField.send_keys(password)
    authorize_form.authorizeButton.click()
    # wait method for changes here
    time.sleep(1)


@then('Successful login for "{email}" and "{password}" is expected to "{pass_or_fail}"')
def step_impl(context, email, password, pass_or_fail):
    # btn_name_after = SearchScreen().authorizeForm.activateAuthorizeButton.text
    actual = SearchScreen().authorizeForm.activateAuthorizeButton.text
    expected = email.split("@")[0]
    Assert.assert_with_condition(actual == expected, pass_or_fail,
                                 message=f"Email={email} and password={password}")
