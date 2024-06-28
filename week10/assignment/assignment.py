"""
Course: CSE 251
Lesson Week: 10
File: assignment.py
Author: <your name>

Purpose: assignment for week 10 - reader writer problem

Instructions:

- Review TODO comments

- writer: a process that will send numbers to the reader.  
  The values sent to the readers will be in consecutive order starting
  at value 1.  Each writer will use all of the sharedList buffer area
  (ie., BUFFER_SIZE memory positions)

- reader: a process that receive numbers sent by the writer.  The reader will
  accept values until indicated by the writer that there are no more values to
  process.  

- Do not use try...except statements

- Display the numbers received by the reader printing them to the console.

- Create WRITERS writer processes

- Create READERS reader processes

- You can use sleep() statements for any process.

- You are able (should) to use lock(s) and semaphores(s).  When using locks, you can't
  use the arguments "block=False" or "timeout".  Your goal is to make your
  program as parallel as you can.  Over use of lock(s), or lock(s) in the wrong
  place will slow down your code.

- You must use ShareableList between the two processes.  This shareable list
  will contain different "sections".  There can only be one shareable list used
  between your processes.
  1) BUFFER_SIZE number of positions for data transfer. This buffer area must
     act like a queue - First In First Out.
  2) current value used by writers for consecutive order of values to send
  3) Any indexes that the processes need to keep track of the data queue
  4) Any other values you need for the assignment

- Not allowed to use Queue(), Pipe(), List(), Barrier() or any other data structure.

- Not allowed to use Value() or Array() or any other shared data type from 
  the multiprocessing package.

- When each reader reads a value from the sharedList, use the following code to display
  the value:
  
                    print(<variable>, end=', ', flush=True)

Add any comments for me:

"""

import random
from multiprocessing.managers import SharedMemoryManager
import multiprocessing as mp
import threading

BUFFER_SIZE = 10
READERS = 2
WRITERS = 2
def reader(sList:SharedMemoryManager.ShareableList, reader_index, items_received_index, rlock: threading.Lock, rSem:threading.Semaphore, wSem:threading.Semaphore):
    while True:
      rlock.acquire()
      rSem.acquire()
      if sList[(sList[reader_index] % BUFFER_SIZE)] == None:
          rSem.release()
          rlock.release()
          break
      print(sList[(sList[reader_index] % BUFFER_SIZE)], end=', ', flush=True)
      sList[items_received_index] += 1
      sList[reader_index] += 1
      rlock.release()
      wSem.release()

    
def writer(sList, writer_index, item_to_be_sent_index, items_received_index, items_to_send, wLock:threading.Lock, rSem:threading.Semaphore, wSem:threading.Semaphore):
    while True:
      wLock.acquire()
      wSem.acquire()
      if items_to_send < sList[item_to_be_sent_index]:
        sList[(sList[writer_index] % BUFFER_SIZE)] = None
        rSem.release()
        wSem.release()
        wLock.release()
        break
      sList[(sList[writer_index] % BUFFER_SIZE)] = sList[item_to_be_sent_index]
      sList[item_to_be_sent_index] += 1
      sList[writer_index] += 1
      rSem.release()
      wLock.release()
def main():

    # This is the number of values that the writer will send to the reader
    items_to_send = random.randint(1000, 10000)

    smm = SharedMemoryManager()
    smm.start()
    # TODO - Create a ShareableList to be used between the processes
    #      - The buffer should be size 10 PLUS at least three other
    #        values (ie., [0] * (BUFFER_SIZE + 3)).  The extra values
    #        are used for the head and tail for the circular buffer.
    #        The another value is the current number that the writers
    #        need to send over the buffer.  This last value is shared
    #        between the writers.
    #        You can add another value to the sharedable list to keep
    #        track of the number of values received by the readers.
    #        (ie., [0] * (BUFFER_SIZE + 4))
    sList = smm.ShareableList([0] * (BUFFER_SIZE + 4))
    reader_index = BUFFER_SIZE
    writer_index = BUFFER_SIZE + 1
    item_to_write_index = BUFFER_SIZE + 2
    items_received_index = BUFFER_SIZE + 3
    items_sent_index = BUFFER_SIZE + 4
    
    sList[reader_index] = 0
    sList[writer_index] = 0
    sList[item_to_write_index] = 1
    sList[items_received_index] = 0

    # TODO - Create any lock(s) or semaphore(s) that you feel you need
    rLock = mp.Lock()
    rSem = mp.Semaphore(0)
    wLock = mp.Lock()
    wSem = mp.Semaphore(BUFFER_SIZE)

    # TODO - create reader and writer processes
    read_processes = [mp.Process(target=reader, args=(sList, reader_index, items_received_index, rLock, rSem, wSem,)) for _ in range(READERS)]
    write_processes =  [mp.Process(target=writer, args=(sList, writer_index, item_to_write_index, items_received_index, items_to_send, wLock, rSem, wSem,))for _ in range(WRITERS)]

    # TODO - Start the processes and wait for them to finish
    for p in read_processes:
       p.start()
    for p in write_processes:
       p.start()
    for p in read_processes:
       p.join()
    for p in write_processes:
       p.join()

    print(f'{items_to_send} values sent')

    # TODO - Display the number of numbers/items received by the reader.
    #        Can not use "items_to_send", must be a value collected
    #        by the reader processes.
    print(f'{sList[items_received_index]} values received')

    smm.shutdown()


if __name__ == '__main__':
    main()
