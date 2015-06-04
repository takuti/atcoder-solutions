name = raw_input()

l = len(name)
if l % 2 == 0: left_head = l/2
else: left_head = l/2 + 1

if name[:l/2] == name[left_head:][::-1]: print 'YES'
else: print 'NO'

