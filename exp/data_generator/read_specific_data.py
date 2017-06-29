import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('data10000.json') as data_file:
  count  = 0;
  for line in data_file:
    data = json.loads(line)
    vehicle = data[u'_source'][u'Vehicle']
    if (('FuelLevel' in vehicle) and ('FuelEfficiency' in vehicle)):
      fuelLevel = vehicle[u'FuelLevel']
      fuelEfficiency = vehicle[u'FuelEfficiency']

      unitData = {}
      unitData['fuelLevel'] = fuelLevel[u'Value']
      unitData['fuelEfficiency'] = fuelEfficiency[u'Value']

      count = count + 1

      print count, unitData
      plt.plot(unitData['fuelLevel'], unitData['fuelEfficiency'], 'ro')

  plt.xlabel('fuel level')
  plt.ylabel('fuel efficiency')
  plt.show()

