f1 = open('gplus_combined.txt', 'r')
f2 = open('fileg.csv', 'w')
for line in f1:
    f2.write(line.replace(' ', ','))
f1.close()
f2.close()


import csv
with open('gpgephi.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(l)