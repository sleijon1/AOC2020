earliest, busses = open("input.txt").read().splitlines()
earliest = int(earliest)
bus_list = busses.split(',')
in_service = [int(bus) for bus in bus_list if bus != 'x']
in_service_copy = list(in_service)
for i, id_ in enumerate(in_service):
    while in_service[i] < earliest:
        in_service[i] += in_service_copy[i]

p1 = (in_service_copy[in_service.index(min(in_service))]) \
    * (min(in_service)-earliest)
print(f"Solution part 1:{p1}")
