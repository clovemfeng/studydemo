#!/usr/bin/python3

def openfile(filename):
  try:
    with open(filename) as fn:
      data = fn.readline()
    return(data.strip().split(','))
  except IOError as ioerror:
    print('File Error:' + str(ioerror))
    return(None)


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


james = openfile('james.txt')
julie = openfile('julie.txt')
mikey = openfile('mikey.txt')
sarah = openfile('sarah.txt')


#james = sorted([sanitize(t) for t in james])
#julie = sorted([sanitize(t) for t in julie])
#mikey = sorted([sanitize(t) for t in mikey])
#sarah = sorted([sanitize(t) for t in sarah])

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

