from functools import reduce
import sys
sys.path.append('../../')
from pyutils.math import crt

_, busses = open("input.txt").read().splitlines()
bus_list = busses.split(',')

in_service = [int(bus) for bus in bus_list if bus != 'x']
distance = [bus_list.index(str(in_service[0]))-bus_list.index(str(id_))
                     for id_ in in_service]
remainder = [id_ + dist for id_, dist in zip(in_service, distance)]
for i, r in enumerate(remainder):
    while True:
        if remainder[i] < 0:
            remainder[i] += in_service[i]
        else:
            break
remainder[0] = 0

solution = crt.crt(in_service, remainder)
print(f"Solution part 2: {solution}")
