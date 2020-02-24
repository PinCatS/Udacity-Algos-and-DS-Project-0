"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getDate(call):
    date, time = call[2].split()
    return date.split('-')

def isCallInMonth(call, month, year):
    call_day, call_month, call_year = getDate(call)
    return  int(call_month) == month and int(call_year) == year

def calls_in_date(calls, month, year):
    calls_list = []
    for call in calls:
        if isCallInMonth(call, month, year):
            calls_list.append(call)

    return calls_list

def get_longest_in(calls, month, year):
    numbers_dict = {}
    for record in calls_in_date(calls, month, year):
        calling, answering, time, duration = record
        if calling in numbers_dict:
            numbers_dict[calling] += int(duration)
        else:
            numbers_dict[calling] = int(duration)
        
        if answering in numbers_dict:
            numbers_dict[answering] += int(duration)
        else:
            numbers_dict[answering] = int(duration)

    max_duration = 0
    max_number = None
    for number in numbers_dict:
        number_duration = numbers_dict[number]
        if number_duration > max_duration:
            max_duration = number_duration
            max_number = number

    return max_number, max_duration

"""
#Tests
#expected ==> (04344)228249 2329
#expected ==> 74066 93594 2629

calls = [['(04344)228249', '(080)43901222', '01-09-2016 06:50:04', '2329'],
['(080)62164823', '74066 93594', '01-09-2016 06:52:07', '300']]

calls = [['(04344)228249', '74066 93594', '01-09-2016 06:50:04', '2329'],
['(080)62164823', '74066 93594', '01-09-2016 06:52:07', '300']]
"""

print("{} spent the longest time, {} seconds, on the phone during September 2016."
            .format(*get_longest_in(calls, 9, 2016)))

"""
Performance
Time: O(n) because functions are run through the list of calls. Access to dict via key should take O(1)
Space: O(n) because we use list and dict structures
"""

