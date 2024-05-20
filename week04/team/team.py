"""
Course: CSE 251
Lesson Week: 04
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

Question: is the Python Queue thread safe?  (https://en.wikipedia.org/wiki/Thread_safety)

"""

import threading
import queue
import requests
import json
import os

# Include cse 251 common Python files
from cse251 import *

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = False  # Special value to indicate no more items in the queue

def retrieve_thread(queue: queue.Queue,  data: list, log:Log):  # TODO add arguments
    """ Process values from the data_queue """
    lock  = threading.Lock()
    while True:
        if NO_MORE_VALUES:
            return
        url = queue.get()
        # TODO make Internet call to get characters name and log it
        log.write(f"Getting request {url}")
        r = requests.get(url)
        r.json()
        name = r['name']
        data.append(name)



def file_reader(queue: queue.Queue, log:Log): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """
    # TODO Open the data file "urls.txt" and place items into a queue
    with open("urls.txt") as file:
        for line in file:
            queue.put(line)
    log.write('finished reading file')
    NO_MORE_VALUES = True
    # TODO signal the retrieve threads one more time that there are "no more values"



def main():
    """ Main function """

    log = Log(show_terminal=True)

    # TODO create queue
    q = queue.Queue()
    data = []

    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job
    t1 = threading.Thread(target=file_reader, args=(q,log,))
    retrieve_threads = []
    for x in range(RETRIEVE_THREADS):
        t = threading.Thread(target=retrieve_thread, args=(q,data, log,))
        retrieve_threads.append(t)
    log.start_timer()

    # TODO Get them going - start the retrieve_threads first, then file_reader
    for t in retrieve_threads:
        t.start()
    t1.start()
    for t in retrieve_threads:
        t.join()
    t1.join()
    # TODO Wait for them to finish - The order doesn't matter
    log.write(data)
    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




