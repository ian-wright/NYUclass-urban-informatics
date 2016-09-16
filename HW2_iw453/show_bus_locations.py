#!//anaconda/bin/python

# Author: Ian Wright
# Purpose: PUI2015 homework 2, assignment 1

import requests
import sys

# my API key: 5a33cebd-8335-4ce4-a891-48c37d2954fe


def get_params():
    """
    Get set of query parameters, and the API endpoint url.
    """
    # get command line args
    caller, key, bus = sys.argv

    # url is hardcoded as the API endpoint
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
    # change API version from default of 1
    version = 2
    # build lineref parameter
    lineref = 'MTA NYCT_' + bus

    print 'Bus Line: ', bus
    return (url, {'key': key, 'version': version, 'LineRef': lineref})


def call_mta_api(url_params):
    """
    Calls the MTA API and parses json response for a list of active buses.
    """
    try:
        resp = requests.get(url_params[0], params=url_params[1])
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)

    # parse out a list of active buses for this route
    bus_list = resp.json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    print 'Number of Active Buses: ', len(bus_list)
    return bus_list


def print_locations(bus_list):
    """
    Iterates through a list of active buses on a given line to print location coordinates for each.
    """
    for count, bus in enumerate(bus_list):
        # get lat and long values for each bus
        lat_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
        long_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])

        # print data to console
        print 'Bus ', count + 1, ' is at Latitude ', lat_loc, ' and Longitude ', long_loc


def main():
        bus_list = call_mta_api(get_params())
        print_locations(bus_list)


if __name__ == '__main__':
    main()
