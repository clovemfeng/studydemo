#!/usr/bin/python3

def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)
  (mins, secs) = time_string.strip().split(splitter)
  return(mins + '.' + secs)

def get_coach_data(filename):
  try:
    with open(filename) as fn:
      data = fn.readline()
    return(data.strip().split(','))
  except IOError as ioerr:
     print('File Error:' + str(ioerr))
     return(None)

sarah = get_coach_data('sarah2.txt')
(sarah_name, sarach_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest time are:"+ 
str(sorted(set([sanitize(t) for t in sarah]))[0:3]))


