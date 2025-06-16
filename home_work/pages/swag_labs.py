from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element('div.login_logo')
            return True
        except NoSuchElementException:
            return False

    def exist_username_field(self):
        try:
            self.find_element('input#user-name')
            return True
        except NoSuchElementException:
            return False

    def exist_password_field(self):
        try:
            self.find_element('input#password')
            return True
        except NoSuchElementException:
            return False