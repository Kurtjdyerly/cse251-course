"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team.py
Author: Brother Comeau

Purpose: Playing Card API calls
Website is: http://deckofcardsapi.com

Instructions:

- Review instructions in I-Learn.

"""

from datetime import datetime, timedelta
import threading
import requests
import json

# Include cse 251 common Python files
from cse251 import *

# TODO Create a class based on (threading.Thread) that will
# make the API call to request data from the website

class Request_thread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        self.response = response.json()
        

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        print('Reshuffle Deck')
        t = Request_thread(f'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/')
        t.start()
        t.join()

    def draw_card(self):
        if self.remaining > 0:
            t = Request_thread(f'https://deckofcardsapi.com/api/deck/{self.id}/draw/')
            t.start()
            t.join()
            if t.response != {}:
                self.remaining = t.response['remaining']
                return t.response['cards'][0]['code']
            else:
                return ''

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = 'eaypesucw83g'

    # Testing Code >>>>>
    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(f'card {i + 1}: {card}', flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

