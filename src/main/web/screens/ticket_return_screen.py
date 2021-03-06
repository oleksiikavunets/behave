from src.main.web.controls.button import Button
from src.main.web.controls.textfield import Field
from selene.api import s
from src.main.web.screens.basescreen import BaseScreen


class TicketReturnScreen(BaseScreen):

    url = 'https://booking.uz.gov.ua/en/cabinet/return_ticket/'

    def __init__(self):
        self.uidField = '#wrapper > div.b-return--form > form > div.fld.uid > div > input'
        self.fcField = '#wrapper > div.b-return--form > form > div:nth-child(3) > input'
        self.lastNameField = '#wrapper > div.b-return--form > form > div:nth-child(4) > input'
        self.firstNameField = '#wrapper > div.b-return--form > form > div:nth-child(5) > input'
        self.returnButton = '#wrapper > div.b-return--form > form > div.button > button'

    def __getattribute__(self, name):
        return globals()[object.__getattribute__(self, 'splitcamel')(name)](s(object.__getattribute__(self, name)))
