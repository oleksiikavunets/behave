from src.main.common import webdriver_config
from selene import browser
from behave import use_fixture


def before_all(context):
    print('\n>>>>BEFORE ALL')
    webdriver_config.configure_driver()


def after_all(context):
    browser.quit()
    print('>>>>AFTER ALL')


def before_feature(context, feature):
    print('    >>>>BEFORE FEATURE')


def after_feature(context, feature):
    print('    >>>>AFTER FEATURE')


def before_scenario(context, scenario):
    print('        >>>>BEFORE SCENARIO')


def after_scenario(context, scenario):
    print('        >>>>AFTER SCENARIO')


def before_step(context, step):
    print('            >>>>BEFORE STEP')


def after_step(context, step):
    print('            >>>>AFTER STEP')