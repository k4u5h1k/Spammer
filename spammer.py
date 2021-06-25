#!/usr/bin/env python3
import re
import sys
import lyricsgenius
from tqdm import tqdm
from time import sleep
from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Whatsapp():
    def __init__(self, contact, message = None, times = None, song = None):
        self.contact = contact
        self.message = message
        self.times = times
        self.song = song

    def _login(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com")
        alert_text = "Open WhatsApp on your phone and scan the QR code within 300 seconds.\nThis alert will dismiss itself in 5 seconds."
        self.driver.execute_script('window.alert(arguments[0])', alert_text)

        try:
            alert = self.driver.switch_to.alert
            sleep(5)
            alert.accept()
        except:
            pass

    def _search_for_contact(self):
        self.wait = WebDriverWait(self.driver, 300)
        search_box = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, search_box))).send_keys(self.contact + Keys.ENTER)

    def _send_message(self, message):
        text_box = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        self.driver.find_element_by_xpath(text_box).send_keys(message + Keys.ENTER)
        sleep(0.01)

    def single_spam(self):
        self._login()
        self._search_for_contact()

        with tqdm(total=self.times, file=sys.stdout, desc="Spamming") as pbar:
            for i in range(self.times):
                self._send_message(self.message)
                pbar.update(1)

    def lyric_spam(self):
        self._login()
        self._search_for_contact()
        genius = lyricsgenius.Genius("G23EEDCAnKeA-0vI-sIzjw3LfXTnxOzaWuKCJ6100G3-0CPT_vy3X5tcw_81ByOw")
        song = genius.search_song(re.sub(' ', '-', self.song))
        lyrics = song.lyrics.split('\n')
        lyrics_warning = f'Does the song start with,\n{lyrics[:2]}? If not, interrupt program in terminal within 20 seconds.'
        lyrics_found = f"lyrics for {self.song} found!"

        if song.lyrics is None or song.lyrics == "":
            print("Song Not Found!")
            return

        print(lyrics_found)
        self.driver.execute_script('window.alert(arguments[0])', lyrics_warning)

        try:
            alert = self.driver.switch_to.alert
            sleep(20)
            alert.accept()
        except:
            pass

        with tqdm(total=len(lyrics), file=sys.stdout, desc="Spamming") as pbar:
            for line in lyrics:
                self._send_message(line)
                pbar.update(1)


if __name__ == '__main__':

    parser = ArgumentParser(description="Only The Most Epic Message Spammer!")
    subparser = parser.add_subparsers(help="available modes, Type mode name followed by -h to see mode specific arguments", dest="mode")
    lyrics_parser = subparser.add_parser('lyrics',help="lyrics spam mode")
    normal_parser = subparser.add_parser('normal',help="single message spam mode")

    lyrics_parser.add_argument("-c", "--contact", required=True, help="exact name of whatsapp contact")
    lyrics_parser.add_argument("-s", "--song", required=True, help="name of song which you want spammed")

    normal_parser.add_argument("-c", "--contact", required=True, help="exact name of whatsapp contact")
    normal_parser.add_argument("-m", "--message", required=True, help="message to spam")
    normal_parser.add_argument("-t", "--times", type=int, default=25, help="number of times the message should be spammed (default 25)")

    args = parser.parse_args()

    if args.mode == "lyrics":
        Whatsapp(contact=args.contact, song=args.song).lyric_spam()
    elif args.mode == "normal":
        Whatsapp(contact=args.contact, message=args.message, times=args.times).single_spam()

    else:
        parser.print_help()
