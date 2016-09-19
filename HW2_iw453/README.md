### PUI 2016 Homework 2
#### Ian Wright ~ iw453

There are two python scripts in this directory:
  - get_bus_info.py
  - show_bus_locations.py
  
Both scripts use the NYC MTA api to get real time data about all buses in the fleet.

*show_bus_locations* takes two command line arguments (an API key, and a bus line), and returns a list of all active buses on that line, along with their current lat and long coordinates. It's called like this:
```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx <BUS_LINE>
```
*get_bus_info* takes an additional command line argument (a filename to write the program's output to), and returns a list of all current buses on the line, along with the name of the NEXT stop for each bus, and a descriptions of the bus' status with respect to that stop. This output is written to standard out, AND written to a simple csv file in the same directory. It's called like this:
```
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <FILE_NAME>.csv
```
Finally, a third file in this directory is called *h2_assign3.ipynb.* This notebook demonstrates reading data from the CUSP datahub directly and programmatically into a pandas dataframe in the python environment. Some simple data cleaning, manipulation, and visualization follows.
