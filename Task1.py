"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_unique(records):
    unique = set()
    for record in records:
        calling, receiving, *_ = record
        unique.add(calling)
        unique.add(receiving)
    
    return unique

 
unique_numbers = get_unique(calls) | get_unique(texts)
print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))