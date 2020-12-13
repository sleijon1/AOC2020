earliest, busses = open("input.txt").read().splitlines()
earliest = int(earliest)
bus_list = busses.split(',')
in_service = [int(bus) for bus in bus_list if bus != 'x']
first = in_service[0]
last = max(in_service)
distance_from_max = [bus_list.index(str(id_))-bus_list.index(str(last))
                     for id_ in in_service]
print(last)

last = (100000000000000//last)*last
while True:
    found = True
    for i, id_ in enumerate(in_service):
        if not ((last + distance_from_max[i]) % id_ == 0):
            found = False
            break
    if found:
        break
    last += max(in_service)*(len(in_service)-1)
print(f"Solution part 2: {last-bus_list.index(str(max(in_service)))}")
