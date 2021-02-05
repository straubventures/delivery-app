# Nathan Straub - ID: 001514364
# I am using the nearest neighbor algorithm, modified with a priority queue based on customer requirements.

from Algo import nearest_neighbor
from TravelTimeFinder import travel_time_finder
from Truck import Truck
from HashTable import HashTable
from DataOrganizer import data_organizer
from PackageLoader import package_loader
from TruckLoader import truck_loader
import csv

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

# An array of the minimum distance for each location.
min_table = []

# An array of dictionaries that each include the values that are under x miles. The keys are the TO locations.
# The index corresponds with the index of that locations matrix in the distances parameter. Thus, the index can be used
# to identify the FROM location.
min_table2 = []


# This code reads the distance table, adds the various locations into a HashTable, and then solves the problem.
with open("WGUPS Distance Table clean.csv") as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    distances = []
    for row in readCSV:
        distances.append(row)

    data_organizer(distances, min_table, min_table2)

# Adds the package data into a hashtable, where the index is the from location, the key is the to location, and the
# value is the package data.
with open("WGUPS Package File clean.csv", encoding="utf-8-sig") as csv_file2:
    readCSV2 = csv.reader(csv_file2, delimiter=',')

    packages = HashTable()
    for row in readCSV2:
        packages.insert(row)

# Initialize trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

trucks = [truck1, truck2, truck3]

# Initialize counter.
z = 0

# Loop through the distances table
while z < len(distances):
    # Loop through the packages and assign each package to a truck using Straub's algorithm.
    package_loader(packages.search(distances[z][0]), packages, trucks, grouped_list, deadline_list, free_and_clear_list,
                   delayed_list, truck_list, load1, load2, load3, every_package)
    z += 1

print("This is the grouped list: " + str(grouped_list) + "\nGrouped length: " + str(len(grouped_list)))
print("This is the deadline list: " + str(deadline_list) + "\nDeadline length: " + str(len(deadline_list)))
print("This is the delayed list: " + str(delayed_list) + "\nDelayed length: " + str(len(delayed_list)))
print("This is the truck list: " + str(truck_list) + "\nTruck length: " + str(len(truck_list)))
print("This is the free and clear list: " + str(free_and_clear_list) + "\nFree and clear length: " + str(
    len(free_and_clear_list)))

print("This is the load1 list: " + str(load1) + "\nLoad1 length: " + str(len(load1)))
print("This is the load2 list: " + str(load2) + "\nLoad2 length: " + str(len(load2)))
print("This is the load3 list: " + str(load3) + "\nLoad3 length: " + str(len(load3)))

master_load = [load1, load2, load3]
master_type = [
    deadline_list,
    grouped_list,
    free_and_clear_list,
    truck_list,
    delayed_list,
    ]


truck_loader(master_load, load1, master_type, distances, min_table2, speed_list, every_package)
truck_loader(master_load, load2, master_type, distances, min_table2, speed_list, every_package)
truck_loader(master_load, load3, master_type, distances, min_table2, speed_list, every_package)

print("Load 1")
for item in load1:
    print(item[0])
print("Load 2")
for item in load2:
    print(item[0])
print("Load 3")
for item in load3:
    print(item[0])

# index 0 is always the address.
# Each location will have the same index for distance information e.g. Hub is always 0, 1060 is always 1, etc.
# Example of working search: print(packages.print_item('5100 South 2700 West'))

print("This is the grouped list: " + str(grouped_list) + "\nGrouped length: " + str(len(grouped_list)))
print("This is the deadline list: " + str(deadline_list) + "\nDeadline length: " + str(len(deadline_list)))
print("This is the delayed list: " + str(delayed_list) + "\nDelayed length: " + str(len(delayed_list)))
print("This is the truck list: " + str(truck_list) + "\nTruck length: " + str(len(truck_list)))
print("This is the free and clear list: " + str(free_and_clear_list) + "\nFree and clear length: " + str(
    len(free_and_clear_list)))

print("This is the load1 list: " + str(load1) + "\nLoad1 length: " + str(len(load1)))
print("This is the load2 list: " + str(load2) + "\nLoad2 length: " + str(len(load2)))
print("This is the load3 list: " + str(load3) + "\nLoad3 length: " + str(len(load3)))

new_load1 = nearest_neighbor(min_table2, load1, distances)
new_load2 = nearest_neighbor(min_table2, load2, distances)
new_load3 = nearest_neighbor(min_table2, load3, distances)



print("New load" + str(new_load1))
print(len(new_load1))
print("New load" + str(new_load2))
print(len(new_load2))
print("New load" + str(new_load3))
print(len(new_load3))
#
# # Calculate all the travel times
travel_time_finder(min_table2, distances, new_load1, travel_times1)

travel_time_finder(min_table2, distances, new_load2, travel_times2)

travel_time_finder(min_table2, distances, new_load3, travel_times3)

# Print the lists of travel times
print(travel_times1)
print(len(travel_times1))
print(len(new_load1))

print(travel_times2)
print(len(travel_times2))
print(len(new_load2))

print(travel_times3)
print(len(travel_times3))
print(len(new_load3))

sum = 0.0
for distance in travel_times1:
    sum += float(distance)

sum2 = 0.0
for distance in travel_times2:
    sum2 += float(distance)

sum3 = 0.0

print()
for distance in travel_times3:
    sum3 += float(distance)

print(sum)

print(sum2)

print(sum3)


print(distances)
print(min_table2)

print("Load 1")
for item in new_load1:
    print(item[0])
print("Load 2")
for item in new_load2:
    print(item[0])
print("Load 3")
for item in new_load3:
    print(item[0])

print("\n")

print(len(every_package))


print(sum + sum2 + sum3)



