lines = open("input.txt").read()
passports = [{field.split(':')[0]:field.split(':')[1]
              for field in line.strip().replace('\n', ' ').split(' ')}
             for line in lines.split('\n\n')]
valid = [pp for pp in passports
         if len(pp.keys()) == 8 or
         len(pp.keys()) == 7
         and 'cid' not in pp.keys()]
print("Solution part 1: ", len(valid))

