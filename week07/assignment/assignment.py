"""
Course: CSE 251
Lesson Week: 07
File: assingnment.py
Author: <Your name here>
Purpose: Process Task Files

Instructions:  See I-Learn

TODO

Add your comments here on the pool sizes that you used for your assignment and
why they were the best choices.


"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
from cse251 import *

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 
def task_prime(value):
    """
    Use the is_prime() above
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    if is_prime(value):
        return (f'{value} is prime')
    else:
        return (f'{value} is not prime')


def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """ 
    with open('words.txt', 'r') as file:
        for line in file:
            if line.strip() == word:
                return (f'{word} Found')
        return (f"{word} not found")
    
        

def task_upper(text: str):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    return (f'{text} ==> uppercase version of {text.upper()}')

def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    total = 0
    for x in range(start_value, end_value):
        total += x
    return (f"sum of {start_value} to {end_value} = {total}")
    

def task_name(url:str ):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return (f'{url} has name {data['name']}')
    else:
        return (f"{url} had an error receiving the information")

    
def main():
    log = Log(show_terminal=True)
    log.start_timer()    

    # TODO Create process pools
    prime_pool = mp.Pool(2)
    word_pool = mp.Pool(3)
    upper_pool = mp.Pool(1)
    sum_pool = mp.Pool(3)
    name_pool = mp.Pool(3)

    output_primes = []
    output_words = []
    output_upper = []
    output_sums = []
    output_names = []

    # TODO you can change the following
    # TODO start and wait pools
    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        # print()
        # print(filename)
        task = load_json_file(filename)
        # print(task)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME:
            output_primes.append(prime_pool.apply_async(task_prime, args=(task['value'], )))
        # 17.6
        if task_type == TYPE_WORD:
            output_words.append(word_pool.apply_async(task_word, args= (task['word'], )))
        # 48.4
        if task_type == TYPE_UPPER:
            output_upper.append(upper_pool.apply_async(task_upper, args= (task['text'], )))
        #  8.9
        if task_type == TYPE_SUM:
            output_sums.append(sum_pool.apply_async(task_sum, args=(task['start'], task['end'], )))
        # 54.5
        if task_type == TYPE_NAME:
            output_names.append(name_pool.apply_async(task_name, args=(task['url'], )))
        # 42.1
        # else:
        #     log.write(f'Error: unknown task type {task_type}')

    result_primes = [p.get() for p in output_primes]
    result_words = [p.get() for p in output_words]
    result_upper = [p.get() for p in output_upper]
    result_sums = [p.get() for p in output_sums]
    result_names = [p.get() for p in output_names]

    # prime_pool.close()
    # prime_pool.join()
    
    # upper_pool.close()
    # upper_pool.join()
    
    # word_pool.close()
    # word_pool.join()

    # sum_pool.close()
    # sum_pool.join()
    
    # name_pool.close()
    # name_pool.join()

    
    # Do not change the following code (to the end of the main function)
    def log_list(lst, log):
        for item in lst:
            log.write(item)
        log.write(' ')
    
    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Number of Primes tasks: {len(result_primes)}')
    log.write(f'Number of Words tasks: {len(result_words)}')
    log.write(f'Number of Uppercase tasks: {len(result_upper)}')
    log.write(f'Number of Sums tasks: {len(result_sums)}')
    log.write(f'Number of Names tasks: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} tasks')

if __name__ == '__main__':
    main()
