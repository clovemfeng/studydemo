#!/usr/bin/python3


def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)
  (mins, secs) = time_string.split(splitter)
  return(mins + '.' + secs)

def unique(userlist):
  unique_user = []
  for each_info in userlist:
    if each_info not in unique_user:
      unique_user.append(each_info)
  print(unique_user[0:3])




with open('james.txt') as jaf:
  data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
  data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
  data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as jaf:
  data = jaf.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])


unique(james)
unique(julie)
unique(mikey)
unique(sarah)
