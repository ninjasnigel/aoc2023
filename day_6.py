races = [54, 94, 64, 92]
records = [302, 1476, 1029, 1404]

races_2 = [54946592]
records_2 = [302147610291404]

def format_data(raw):
    return raw, raw

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

from elis_script import *

if __name__ == '__main__':
    main(format_data, star1, star2)