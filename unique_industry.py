#Purpose of this file was to check how many unique industries were present. It's a lot.

import csv
import os

industry = []

def uniqueEntry(tick):
    for x in industry:
        if x == tick:
            return 0
    return 1

with open("stocks-list.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if uniqueEntry(row['Industry']):
            industry.append(row['Industry'])

parent_dir = './industry/'
for x in industry:
    if(x == 'Blank Check / SPAC'): open(parent_dir + 'SPAC.csv','w').close()
    elif(x == 'n/a'): open(parent_dir + 'NA.csv','w').close()
    else: 
        path = os.path.join(parent_dir,x + '.csv')
        open(path,'w').close()

with open('unique_industry.txt', 'w') as f:
    for x in industry:
        f.write(x)
        f.write('\n')
f.close()