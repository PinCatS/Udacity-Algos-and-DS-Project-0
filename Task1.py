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

"""
# Tests
records1 = [['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
            ['90087 42537', '(080)35121497', '01-09-2016 06:17:26', '573']]

# expected ==> ('93427 40118', '(080)33118033', '90087 42537', '(080)35121497')
# expected ==> 4
print(get_unique_telephone_numbers(records1))
print(len(get_unique_telephone_numbers(records1)))

records2 = [['(080)33118033', '(080)33118033', '01-09-2016 06:11:23', '1156'],
            ['(080)33118033', '(080)33118033', '01-09-2016 06:17:26', '573']]

# expected ==> ((080)33118033')
# expected ==> 1

print(get_unique_telephone_numbers(records2))
print(len(get_unique_telephone_numbers(records2)))"""

unique_from_calls = get_unique(calls)
unique_from_texts = get_unique(texts)
unique_total = len(unique_from_calls) + len(unique_from_texts)
print("There are {} different telephone numbers in the records.".format(unique_total))

"""
Time: O(n) because we need to run through all records and add them to the set
Space: O(n) because uses set to store unique calls
"""