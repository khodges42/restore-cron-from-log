import sys
from datetime import datetime
from dateutil import parser
lines = []
full_log = []
with open(sys.argv[1]) as f:
    for line in f:
        splitline = line.split()
        full_log.append(line)
        lines.append(' '.join(splitline[5:]))

print set(lines)

for item in set(lines):
    timescron = [i for i, x in enumerate(lines) if x == item]
    timesrun = []
    for time in timescron:        
        timesrun.append(parser.parse(' '.join(full_log[time].split()[:3])))
    if len(timesrun) > 1:
        print "---------------{}-----------".format(item)
        print timesrun[1] - timesrun[0]
    else:
        print"=============================={} was only run once".format(item)
