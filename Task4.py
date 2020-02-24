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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def extract(calls):
    outgoing = set()
    receiving = set()
    for call in calls:
        outgoing_number, receiving_number, *_ = call
        outgoing.add(outgoing_number)
        receiving.add(receiving_number)
    
    return outgoing, receiving

outgoing_calls, receiving_calls = extract(calls)
outgoing_texts, receiving_texts = extract(texts)
telemarketers = (receiving_texts | receiving_calls) & (outgoing_calls - outgoing_texts)

telemarketers_list = list(telemarketers)
telemarketers_list.sort()

for telemarketer in telemarketers_list:
    print(telemarketer)

"""
Efficiency analysis

    extract() has time O(n) because it iterates through all calls/texts
    extract() requires space O(2n) ==> O(n)

    Task 4 has time O(nlogn): to be more specific
        extracts ==> O(2n)
        union ==> O(len(r_t) + len(r_c))
        difference ==> O(len(o_c))
        intersect ==> O(min(x1, x2))
        
        list from set ==> O(n)
        sort ==> O(nlogn)
        in ==> O(n)

    Task 4 has space O(n): to be more specific:
        extract() ==> O(2n)

        4 sets of numbers ==> O(4n)
        telemarketers ==> O(n)
        list ==> O(n)
        Their sum ==> O(4n) + O(n) + O(n) ==> O(6n)
"""

