# Nathan Straub - ID: 001514364
# I am using the nearest neighbor algorithm, modified with a priority queue based on customer requirements.

from Algo import nearest_neighbor
from CreateGraph import create_graph
from TravelTimeFinder import travel_time_finder
from HashTable import HashTable
from PackageLoader import package_loader
from TruckLoader import truck_loader
import csv
from datetime import *

every_package = []

# Used for testing truck_loader
speed_list = []

travel_times1 = []
travel_times2 = []
travel_times3 = []

# Used for testing PackageLoader
grouped_list = []
deadline_list = []
free_and_clear_list = []
delayed_list = []
truck_list = []

# Lists of loads
load1 = []
load2 = []
load3 = []

distances = []

min_table = {}

# This code reads the distance table, adds the various locations into a HashTable, and then solves the problem.
with open("WGUPS Distance Table clean.csv") as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:
        distances.append(row)


min_table = create_graph(distances, min_table)

# Adds the package data into a hashtable, where the index is the from location, the key is the to location, and the
# value is the package data.
with open("WGUPS Package File clean.csv", encoding="utf-8-sig") as csv_file2:
    readCSV2 = csv.reader(csv_file2, delimiter=',')

    packages = HashTable()
    for row in readCSV2:
        packages.insert(row)





# Initialize counter.
z = 0

# Loop through the distances table
while z < len(distances):
    # add packages to each load using a priority algorithm
    package_loader(packages.search(distances[z][0]), packages, grouped_list, deadline_list, free_and_clear_list,
                   delayed_list, truck_list, load1, load2, load3, every_package)
    z += 1


master_load = [load1, load2, load3]
master_type = [
    deadline_list,
    grouped_list,
    free_and_clear_list,
    truck_list,
    delayed_list,
    ]

# add all the remaining packages
truck_loader(master_load, min_table, every_package)


# index 0 is always the address.
# Each location will have the same index for distance information e.g. Hub is always 0, 1060 is always 1, etc.
# Example of working search: print(packages.print_item('5100 South 2700 West'))

# create efficiently navigated paths for each load
new_load1 = nearest_neighbor(min_table, load1, distances)
new_load2 = nearest_neighbor(min_table, load2, distances)
new_load3 = nearest_neighbor(min_table, load3, distances)

# make some adjustments so that the third load can leave on time.
new_load2.insert(1, new_load3[2])
new_load3.remove(new_load3[2])

new_load2.insert(1, new_load3[1])
new_load3.remove(new_load3[1])

# # Calculate all the travel times
travel_time_finder(min_table, new_load1, travel_times1)
travel_time_finder(min_table, new_load2, travel_times2)
travel_time_finder(min_table, new_load3, travel_times3)

sum = 0.0
for distance in travel_times1:
    sum += float(distance)

sum2 = 0.0
for distance in travel_times2:
    sum2 += float(distance)

sum3 = 0.0
for distance in travel_times3:
    sum3 += float(distance)

new_master_load = [new_load1, new_load2, new_load3]

# Add delivery status to each item in the load lists.
for truckload in new_master_load:
    for package in truckload:
        package.append("At Hub")

all_sum = sum + sum2 + sum3

# Initiate start times for the trucks

truck2_start = timedelta(0,0,0,0,0,8)
truck1_start = timedelta(0,0,0,0,5,9)



# update the status of each of package when they are delivered.
for i, time in enumerate(travel_times1):
    truck2_start += timedelta(0,0,0,0,0,(float(float(travel_times1[i]) /18)))
    if time is not None:
        if len(new_load1[i]) > 4:
            new_load1[i][8] = "Delivered"
            new_load1[i].append(truck1_start)



for i, time in enumerate(travel_times2):
    truck1_start += timedelta(0,0,0,0,0,(float(float(travel_times2[i]) /18)))
    if len(new_load2[i]) > 4:
        new_load2[i][8] = "Delivered"
        new_load2[i].append(truck2_start)


# uses truck2 start because they are the same truck

for i, time in enumerate(travel_times3):
    truck2_start += timedelta(0,0,0,0,0,(float(float(travel_times3[i]) /18)))
    if len(new_load3[i]) > 4:
        new_load3[i][8] = "Delivered"
        new_load3[i].append(truck1_start)


print("The total distance traveled: " + str(all_sum))

truck1_start = timedelta(0,0,0,0,0,8)
truck2_start = timedelta(0,0,0,0,5,9)
truck3_start = timedelta(0,0,0,0,0,10)

truck_times = [truck1_start, truck2_start, truck3_start]

# add delivery status to hash table.
for load in master_load:
    packages.insert_delivery_status(load)

# User interface
while 0 < 1:
    report = input("Type the package ID you wish to check on: ")
    if report == 'exit':
        exit(0)
    else:
        for lo, load in enumerate(new_master_load):
            for package in load:
                if str(package[0]).lstrip() == report:
                    print(package)
                    hour = input("For what time would you like this package's status? Please type the hour first: ")
                    minute = input("And now the minutes: ")
                    requested_time = timedelta(0,0,0,0,int(minute), int(hour)).seconds
                    if truck_times[lo].seconds < requested_time < package[9].seconds:
                        print("Package is en route at " + str(hour) + ":" + str(minute))
                        break
                    elif requested_time > package[9].seconds:
                        print("Package was delivered at " + str(package[9]))
                        break
                    else:
                        print("Package is at the Hub at " + str(hour) + ":" + str(minute))
                        break

                else: continue