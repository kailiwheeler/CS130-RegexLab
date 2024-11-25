import urllib.request
import re

def ascii_histogram(seq) -> None: #create a histogram from a list of numbers
    counted = count_elements(seq) #generate frequency table (dictionary)
    for key in sorted(counted):
        plus_str = '+' * counted[key]
        print(f'{key} {plus_str}') #prints out asterisk
def count_elements(seq): #creates a dictionary
    hist = dict()
    for date in seq:
        hist[date]=hist.get(date,0)+ 1
    return hist

hand = open('TE.txt', encoding='utf-8')
lyrs = []
for line in hand:
    yrs = re.findall(r'.([1-2][0|8|9][0-9][0-9])', line)
    for elm in yrs:
        lyrs.append(elm)
ascii_histogram(lyrs)
