#!/usr/bin/env python3
import sys
from time import sleep
import lyricsgenius
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class Whatsapp():
    def __init__(self, contact, message = None, times = None, song = None):
        self.url = "https://web.whatsapp.com"
        self.search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
        self.alert_text = "Open WhatsApp on your phone and scan the QR code within 300 seconds.\nThis alert will dismiss itself in 5 seconds."
        self.text_box = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        self.contact = contact
        self.message = message
        self.times = times
        self.song = song

    def _login(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.execute_script('window.alert(arguments[0])', self.alert_text)
        try:
            alert = self.driver.switch_to.alert
            sleep(5)
            alert.accept()
        except:
            pass

        print("Logged In")

    def _search_for_contact(self):
        self.wait = WebDriverWait(self.driver, 300)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search))).send_keys(self.contact + Keys.ENTER)
        print("Found contact")

    def _send_message(self, message):
        self.driver.find_element_by_xpath(self.text_box).send_keys(message + Keys.ENTER)
        sleep(0.01)

    def single_spam(self):
        self._login()
        self._search_for_contact()
        print("Spamming")
        for i in range(self.times):
            self._send_message(self.message)

    def lyric_spam(self):
        self._login()
        self._search_for_contact()
        genius = lyricsgenius.Genius("G23EEDCAnKeA-0vI-sIzjw3LfXTnxOzaWuKCJ6100G3-0CPT_vy3X5tcw_81ByOw")
        song = genius.search_song(self.song)
        lyrics = song.lyrics.split('\n')

        if song.lyrics is None or song.lyrics == "":
            print("Song Not Found!")
            return

        print("lyrics for",self.song,"found!")
        self.driver.execute_script('window.alert(arguments[0])', f'Does you song start with,\n{lyrics[:2]}? If not interrupt program within 20 seconds.')

        try:
            alert = self.driver.switch_to.alert
            sleep(20)
            alert.accept()
        except:
            pass

        print("Spamming")
        for line in lyrics:
            self._send_message(line)

if __name__ == '__main__':
    parser = ArgumentParser()    
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-n", "--normal", action="store_true", help = "normal single message spam mode")
    mode.add_argument("-l", "--lyrics", action="store_true", help = "song lyrics spam mode")
    parser.add_argument("-c", "--contact", required = True, help = "exact name of whatsapp contact (required)")
    parser.add_argument("-m", "--message", help = "message to spam (only if using normal mode)")
    parser.add_argument("-t", "--times", type = int, help = "number of times the message should be spammed (only if using normal mode)")
    parser.add_argument("-s", "--song", help = "name of song which you want spammed(only if using lyrics mode)")
    arg = parser.parse_args()

    if arg.lyrics:
        Whatsapp(contact=arg.contact, song = arg.song).lyric_spam()
    else:
        Whatsapp(contact=arg.contact, message=arg.message, times = arg.times).single_spam()
