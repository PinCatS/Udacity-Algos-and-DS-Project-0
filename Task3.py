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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extract_code(number):
	code = None

	if number.startswith('(0'):
		code = number[0:number.index(')') + 1]
	elif number.startswith('7') or number.startswith('8') or number.startswith('9'):
		code = number[:4]
	elif number.startswith('140'):
		code = '140'

	return code


def isFrom(number, code):
	return extract_code(number) == code


def get_called_from(calls, code):
	called_from_code_list = []
	for call in calls:
		calling, answering, *_ = call
		if isFrom(calling, code):
			 called_from_code_list.append(extract_code(answering))
	
	return called_from_code_list

"""
Returns percentage of code in codes
"""
def percentage_of(codes, code):
	return codes.count(code) / len(codes) * 100

BANGALOR_CODE = '(080)'

codes = get_called_from(calls, BANGALOR_CODE)
unique_codes = set(codes)
unique_codes_list = list(unique_codes)
unique_codes_list.sort()


print("The numbers called by people in Bangalore have codes:")
for code in unique_codes_list:
   print(code)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
 				.format(percentage_of(codes, BANGALOR_CODE)))