races = [54, 94, 64, 92]
records = [302, 1476, 1029, 1404]

races_2 = [54946592]
records_2 = [302147610291404]

def format_data(raw):
    return raw

def get_record_breakers(races, records):
    records_breakers = []
    for i,race in enumerate(races):
        race_speeds = []
        breaker = 0
        for speed in range(race):
            race_speeds += [(race - speed)*speed]
        for speed in race_speeds:
            if speed > records[i]:
                breaker += 1
        records_breakers += [breaker]
    return records_breakers
    
def star1(data):
    record_breakers = get_record_breakers(races, records)
    mulsum = 1
    for breaker in record_breakers:
        if breaker: mulsum *= breaker
    return(mulsum)

def star2(data):
    return get_record_breakers(races_2, records_2)[0]

# -----------------------------------------------------------------------------------------
# Elis script grejer här under ;) https://github.com/eliskleen/AOC/blob/master/2023/day_.py

import os
import sys
import time
from aocd import submit
from aocd.models import Puzzle
import itertools
import functools


def day_():
    year = int(os.getcwd().split('\\')[-1][3:7]) 
    day = int(__file__.split('\\')[-1].split('_')[1].split('.')[0])
    puzzle = Puzzle(year=year, day=day) 
    submit_a = "a" in sys.argv
    submit_b = "b" in sys.argv
    example = "e" in sys.argv

    if (submit_a or submit_b) and example:
        print("Cannot submit examples")
        return

    raw_data = puzzle.input_data
    if example:
        print("Using example")
        #use 'aocd year day --example' to get the example data
        with open('example.txt', 'r') as f:
            raw_data = f.read()

            
    start_time = time.perf_counter()
    data = format_data(raw_data)

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2(data)
    time3 = time.perf_counter()

    load_time = time1 - start_time
    star1_time = time2 - time1
    star2_time = time3 - time2

    if submit_a:
        print("Submitting star 1")
        puzzle.answer_a = ans1
    if submit_b:
        print("Submitting star 2")
        puzzle.answer_b = ans2
    if 1:
        print(f'Load time: {load_time}')
        print(f'Star 1 time: {star1_time}')
        print(f'Star 2 time: {star2_time}')
        print(f'Star 1 answer: {ans1}')
        print(f'Star 2 answer: {ans2}')

def main():
    import cProfile
    import pstats
    with cProfile.Profile() as pr:
        day_()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    day = int(__file__.split('\\')[-1].split('_')[1].split('.')[0])
    stats.dump_stats(filename = f'profiling\\profiling{day}.prof')

# run with `py day_n.py -- a b` to submit both stars for day n
if __name__ == '__main__':
    main()