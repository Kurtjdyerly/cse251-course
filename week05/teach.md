![](../site/banner.png)

# 05 Teach: Using Semaphores, Queue and List

## Instructions

**Face-to-face** students will complete this activity in class.

**Online students** should arrange for a one hour synchronous meeting to work through the activity together.

## Overview

Your team will be creating thread and processes to check a list of prime numbers from a file.

## Assignment

The following graph outlines the processes and data structures that you will need to solve this program.

![](team_graph.png)

**data.txt** This is the file that contains a list of numbers to test if they are prime.

**Reader Thread** This is a thread that will read the data file and place items onto a Queue. (Hint: a semaphore is also required here)

**Queue** This is a multiprocessing Queue.

**Prime Process** This is a process that will read something from the Queue and check to see if it is a prime number.  If the number is prime, it will place the number on a shared list.  You need 3 of these processes.

**List of Primes** This is a shared List that will contain the prime numbers

**Main** This is the main code that will create the thread, processes, queue, semaphore(s), and list.  It will display all of the prime numbers after the `prime process`'s are finished.


### Requirements

1. Read the numbers from the data file into a queue.
2. Create three `prime processes`'s that will test the numbers from the queue
3. Do not hard code the number of values that the program will process. Your program needs to handle any number of values in a data file.
4. Get main to display the final list of prime numbers.
5. After you get the program working, change it to handle any number of `prime process` processes.

## Sample Solution

We will go over the solution in the next class lesson.

## Submission

When complete, please report your progress in the associated I-Learn quiz.
