#!/usr/bin/python3

def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)
  (mins, secs) = time_string.strip().split(splitter)
  return(mins + ':' + secs)


def get_cocah_data(filename):
  try:
    with open(filename) as fn:
      data = fn.readline()
      user_data = data.strip().split(',')
      return ({
      'Name': user_data.pop(0),
      'Bob' : user_data.pop(0),
      'Times':str(sorted(sanitize(t) for t in user_data)[0:3])
      })
  except IOError as ioerr:
    print('File Error:' + str(ioerr))
    return(None)

sarah = get_cocah_data('sarah2.txt')
print(sarah['Name'] + "'s fastest time is:" + sarah['Times'])
