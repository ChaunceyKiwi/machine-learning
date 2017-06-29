import json
from pprint import pprint
import matplotlib.pyplot as plt

f = open('rpm_speed_10K.txt', 'w+')

with open('data10000.json') as data_file:
  count  = 0;
  for line in data_file:
    data = json.loads(line)
    vehicle = data[u'_source'][u'Vehicle']
    if (('RPM' in vehicle) and ('Speed' in vehicle)):
      rpm = vehicle[u'RPM']
      speed = vehicle[u'Speed']

      unitData = {}
      unitData['rpm'] = rpm[u'Value']
      unitData['speed'] = speed[u'Value']

      count = count + 1

      # print count, unitData
      plt.plot(unitData['rpm'], unitData['speed'], 'r.') 
      s = str(unitData['rpm']) + "," + str(unitData['speed']) + "\n"
      f.write(s)
      print count

  plt.xlabel('rpm')
  plt.ylabel('speed')
  plt.show()

