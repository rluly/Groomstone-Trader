#Purpose of this file was to check how many unique industries were present. It's a lot.

import csv

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

print(industry)