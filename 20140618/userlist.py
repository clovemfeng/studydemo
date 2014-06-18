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


def get_cocah_data(filename):
  try:
    with open(filename) as fn:
      data = fn.readline()
    return(data.strip().split(','))
  except IOError as ioerr:
    print('File Error:' + str(ioerr))
    return(None)






sarah = get_cocah_data('sarah2.txt')
print(sarah)
sarah_data = {}

sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] =  sarah.pop(0)
sarah_data['Times']= sarah

print(sarah_data)
print('=========')

print(sarah_data['Name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
