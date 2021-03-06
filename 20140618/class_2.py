#!/usr/bin/python3

class Athlete():
  def __init__(self, a_name, a_dob=None, a_times=[]):
    self.name = a_name
    self.dob = a_dob
    self.times = a_times
  def top3(self):
    return(sorted(set([sanitize(t) for t in self.times]))[0:3])

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
    with open(filename) as f:
      data = f.readline()
    tmp1 = data.strip().split(',')
    return(Athlete(tmp1.pop(0),tmp1.pop(0), tmp1))
  except IOError as ioerr:
     print('File Error:' + str(ioerr))
     return(None)

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are:"+ str(james.top3()))
