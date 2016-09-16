#!//anaconda/bin/python

import requests
import sys

# my API key: 5a33cebd-8335-4ce4-a891-48c37d2954fe

# get command line args
caller, key, bus = sys.argv

# url is hardcoded as the API endpoint
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
# change API version from default of 1
version = 2
# build lineref parameter
lineref = 'MTA NYCT_' + bus

# make API request
params = {'key': key, 'version': version, 'LineRef': lineref}
try:
    resp = requests.get(url, params=params)
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

# parse out a list of active buses for this route
bus_list = resp.json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print 'Bus Line: ', bus
print 'Number of Active Buses: ', len(bus_list)

bus_count = 1
for bus in bus_list:
    # get lat and long values for each bus
    lat_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])

    # print data to console
    print 'Bus ', bus_count, ' is at Latitude ', lat_loc, ' and Longitude ', long_loc

    bus_count += 1
