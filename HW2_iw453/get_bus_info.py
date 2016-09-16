#!//anaconda/bin/python

# Author: Ian Wright
# Purpose: PUI2015 homework 2, assignment 2

import requests
import sys
import pandas as pd

# my API key: 5a33cebd-8335-4ce4-a891-48c37d2954fe


def get_params():
    """
    Get set of query parameters, and the API endpoint url.
    """
    # get command line args
    caller, key, bus, FileName = sys.argv

    # url is hardcoded as the API endpoint
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
    # change API version from default of 1
    version = 2
    # build lineref parameter
    LineRef = 'MTA NYCT_' + bus
    # toggle the call(stop)-level data to ON
    VehicleMonitoringDetailLevel = 'calls'

    return (url, {'key': key, 'version': version, 'LineRef': LineRef, 'VehicleMonitoringDetailLevel': VehicleMonitoringDetailLevel})


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
    return resp.json()['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


def build_dataframe(bus_list):
    """
    Uses query response to build a pandas dataframe of the relevant bus data.
    """
    # intialize a pandas dataframe to contain stop data
    df = pd.DataFrame(columns=['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

    for i, bus in enumerate(bus_list):
        # get lat and long values for each bus
        lat_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
        long_loc = '{0:.6f}'.format(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        # get next stop name and current vehicle status
        # if there are no Onward Calls on record for the bus, use N/A for name and status
        if not bus['MonitoredVehicleJourney']['OnwardCalls']:
            stop_name = 'N/A'
            stop_status = 'N/A'
        else:
            next_stop = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
            stop_name = next_stop['StopPointName'][0]
            stop_status = next_stop['ArrivalProximityText']

        # append new row of data to dataframe
        df.loc[i] = [lat_loc, long_loc, stop_name, stop_status]

    return df


def main():

    bus_list = call_mta_api(get_params())
    df = build_dataframe(bus_list)

    print df
    print 'csv file created.'
    df.to_csv(sys.argv[3] + '.csv', index=False)


if __name__ == '__main__':
    main()
