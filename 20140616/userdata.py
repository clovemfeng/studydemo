#!/usr/bin/python3

def santitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in  time_string:
    splitter = ':'
  else:
    return(time_string)
  (mins, secs) = time_string.split(splitter)
  return(mins + '.' + secs)

clean_james = []
clean_julie = []
clean_sarah = []
clean_mikey = []

with open('james.txt') as jaf:
  data = jaf.readline()
  clean_james = data.strip().split(',')
with open('julie.txt') as juf:
  data = juf.readline()
  clean_julie = data.strip().split(',')
with open('sarah.txt') as saf:
  data = saf.readline()
  clean_sarah = data.strip().split(',')
with open('mikey.txt') as mif:
  data = mif.readline()
  clean_mikey = data.strip().split(',')

'''for each_t in james:
  clean_james.append(santitize(each_t))
for each_t in julie:
  clean_julie.append(santitize(each_t))
for each_t in mikey:
  clean_mikey.append(santitize(each_t))
for each_t in sarah:
  clean_sarah.append(santitize(each_t))
'''




print(sorted(santitize(each_t) for each_t in clean_james))
print(sorted(santitize(each_t) for each_t in clean_julie))
print(sorted(santitize(each_t) for each_t in clean_sarah))
print(sorted(santitize(each_t) for each_t in clean_mikey))
