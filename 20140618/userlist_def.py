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
      user = data.strip().split(',')
      return({'Name': user.pop(0),
              'Dob' : user.pop(0),
	      'Times':str(sorted(set([sanitize(t) for t in user]))[0:3])
	      })
  except IOError as ioerr:
    print('File Error:' + str(ioerr))
    return(None)






james = get_cocah_data('james2.txt')
print(james['Name'] + "'s fastest times are:" + james['Times'])
