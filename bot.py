import argparse
import getpass
import json
import time
import smtplib
import sys
from datetime import datetime as dt

from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


TIME_FORMAT = r'%Y-%m-%d-%H-%M-%S'


class FSUBot(object):
    def __init__(self, start_page_url, fsuid='', fsupw='', auto_login=True, browser='chrome'):
        self.SLEEP_TIME = 1.5

        self.fsuid = input('FSU-ID: ') if not fsuid else fsuid
        self.fsupw = getpass.getpass() if not fsupw else fsupw

        if browser.lower() == 'firefox':
            self.dr = webdriver.Firefox()
        else:
            self.dr = webdriver.Chrome('./chromedriver')

        if auto_login:
            self.my_fsu_login()
        self.dr.get(start_page_url)

    def my_fsu_login(self):
        FSU_LOGIN_URL = 'https://cas.fsu.edu/cas/login?service=https://my.fsu.edu'

        self.dr.get(FSU_LOGIN_URL)
        username = self.dr.find_elements_by_class_name("loginInput")[0]
        password = self.dr.find_elements_by_class_name("loginInput")[1]

        time.sleep(self.SLEEP_TIME)
        print("Entering login credentials...")

        username.send_keys(self.fsuid)
        password.send_keys(self.fsupw)
        time.sleep(self.SLEEP_TIME)

        print("Attempting to login...")
        login_button = '#fm2 > table > tbody > tr:nth-child(2) > td:nth-child(6) > input'
        self.dr.find_elements_by_css_selector(login_button)[0].click()
        time.sleep(self.SLEEP_TIME * 2)

    def navigate(self, filename=None, jsonlist=None):
        if filename:
            with open(filename) as f:
                json_list = json.load(f)

        if json_list:
            for item in json_list:
                self._navigate(**item)
        else:
            raise RuntimeError('No JSON list of navigation points provided.')

    def _navigate(self, title=None, xpath=None, css_selector=None):
        time.sleep(self.SLEEP_TIME * 2)
        if title:
            print("Navigating to " + title + "...")

        if xpath:
            elem = self.dr.find_elements_by_xpath(xpath)[0]
        elif css_selector:
            elem = self.dr.find_elements_by_css_selector(css_selector)[0]
        else:
            raise Exception("Unable to navigate without xpath or " \
                            "css selector.")
        elem.click()

        if title:
            print("Navigation succeeded.")

    def _focus_iframe(self, title, xpath=None, css_selector=None):
        if title:
            print("Focusing on " + title + "'s iFrame...")
        if xpath:
            frame = self.dr.find_elements_by_xpath(xpath)[0]
        elif css_selector:
            frame = self.dr.find_elements_by_css_selector(css_selector)[0]
        self.dr.switch_to.frame(frame)
        print("Frame-switch succeeded.")
        time.sleep(self.SLEEP_TIME)


    def main_loop(self):
        pass

    @property
    def page_source(self):
        return self.dr.page_source.encode('utf-8')

    def element_exists(self, xpath):
        try:
            return bool(self.dr.find_elements_by_xpath(xpath))
        except:
            return False


def _main(nav_list_json=None, main_loop=None):
    """
    :param nav_list: list of
    :type nav_list: list

    """
    STUDY_ROOMS_URL = 'https://www.lib.fsu.edu/dirac-study-rooms'

    bot_description = 'StudyRoomBot'

    parser = argparse.ArgumentParser(description=vindicta_description)
    parser.add_argument('-f', '--fsu-id',
                        help='Username for the student\'s MyFSU account.',
                        required=False)
    parser.add_argument('-p', '--password',
                        help='Password for the student\'s MyFSU account.',
                        required=False)
    args = parser.parse_args()

    if args.fsu_id and not args.password:
        parser.error('MyFSU ID given, but no password specified.')
    elif not args.fsu_id and args.password:
        parser.error('MyFSU password given, but no ID specified.')

    fsu_dr = FSUBot(args.fsu_id, args.password, STUDY_ROOMS_URL)
    fsu_dr.login_to_fsu()
    fsu_dr.navigate(filename=nav_list_json)
    fsu_dr.main_loop()


if __name__ == "__main__":
    _main()
