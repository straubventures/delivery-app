# Nathan Straub - ID: 001514364
# I am using the nearest neighbor algorithm, modified with a priority queue based on customer requirements.

from DistancesMatrix import load_distances
from Truck import Truck
from HashTable import HashTable
from DataOrganizer import data_organizer
from PackageLoader import package_loader
import csv

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

# This code reads the distance table, adds the various locations into a HashTable, and then solves the problem.
with open("WGUPS Distance Table clean.csv") as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    distances = []
    for row in readCSV:
        distances.append(row)

    data_organizer(distances)

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

# Print the full package hash table.
print(packages.print("Hello"))

# Initialize counter.
z = 0

# Loop through the distances table
print("This is the package loader")
while z < len(distances):
    print("This is the input to package loader: " + str(distances[z][0]))

    # Loop through the packages and assign each package to a truck using Straub's algorithm.
    package_loader(packages.search(distances[z][0]), packages, trucks, grouped_list, deadline_list, free_and_clear_list, delayed_list, truck_list, load1, load2, load3)
    z += 1

print("This is the grouped list: " + str(grouped_list) + "\nGrouped length: " + str(len(grouped_list)))
print("This is the deadline list: " + str(deadline_list) + "\nDeadline length: " + str(len(deadline_list)))
print("This is the delayed list: " + str(delayed_list) + "\nDelayed length: " + str(len(delayed_list)))
print("This is the truck list: " + str(truck_list) + "\nTruck length: " + str(len(truck_list)))
print("This is the free and clear list: " + str(free_and_clear_list) + "\nFree and clear length: " + str(len(free_and_clear_list)))

print("This is the load1 list: " + str(load1) + "\nLoad1 length: " + str(len(load1)))
print("This is the load2 list: " + str(load2) + "\nLoad2 length: " + str(len(load2)))
print("This is the load3 list: " + str(load3) + "\nLoad3 length: " + str(len(load3)))

while len(load1) < 16:
    for item in deadline_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load1) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This deadline item was found for load 1: " + str(item))
            load1.append(item)
            deadline_list.remove(item)
        else:
            print(str(item) + " deadline item  was rejected from 1.")
    for item1 in grouped_list:
        if item1 in load1 or item1 in load2 or item1 in load3:
            grouped_list.remove(item1)
        elif len(load1) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This grouped item was found: " + str(item1))
            load1.append(item1)
            grouped_list.remove(item1)
        else:
            print(str(item1) + " grouped item was rejected from 1.")
            continue
    for item in delayed_list:
        if item in load1 or item in load2 or item in load3:
            delayed_list.remove(item)
        elif len(load1) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found for 1: " + str(item))
            load1.append(item)
            delayed_list.remove(item)
        else:
            print(str(item) + " was rejected for 1.")
    for item in truck_list:
        if item in load1 or item in load2 or item in load3:
            truck_list.remove(item)
        elif len(load1) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load1.append(item)
            truck_list.remove(item)
            print(truck_list)
        else:
            print(str(item) + " was rejected for 1.")
    for item in free_and_clear_list:
        if item in load1 or item in load2 or item in load3:
            free_and_clear_list.remove(item)
        elif len(load1) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This free and clear item was found for load 1: " + str(item))
            load1.append(item)
            free_and_clear_list.remove(item)
        else:
            print(str(item) + " was rejected for 1.")

while len(load2) < 16:
    for item in deadline_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load2) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load2.append(item)
            deadline_list.remove(item)
        else:
            print(str(item) + " was rejected from 2.")
    for item in grouped_list:
        if item in load1 or item in load2 or item in load3:
            grouped_list.remove(item)
        elif len(load2) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found for 2: " + str(item))
            load2.append(item)
            grouped_list.remove(item)
        else:
            print(str(item) + " was rejected for 2.")
    for item in delayed_list:
        if item in load1 or item in load2 or item in load3:
            delayed_list.remove(item)
        elif len(load2) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found for 2: " + str(item))
            load2.append(item)
            delayed_list.remove(item)
        else:
            print(str(item) + " was rejected for 2.")
    for item in truck_list:
        if item in load1 or item in load2 or item in load3:
            truck_list.remove(item)
        elif len(load2) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load2.append(item)
            truck_list.remove(item)
            print(truck_list)
        else:
            print(str(item) + " was rejected for 2.")
    for item in free_and_clear_list:
        if item in load1 or item in load2 or item in load3:
            free_and_clear_list.remove(item)
        elif len(load2) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This free and clear item was found: " + str(item))
            load2.append(item)
            free_and_clear_list.remove(item)
        else:
            print(str(item) + " was rejected for 2.")

while (len(load1) + len(load2) + len(load3)) < 40:
    for item in deadline_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load3) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found in deadlines: " + str(item))
            load3.append(item)
            deadline_list.remove(item)
            print("Item was deleted!")
        else:
            print(str(item) + " was rejected for 3 deadline.")
    for item in grouped_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load3) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load3.append(item)
            grouped_list.remove(item)
        else:
            print(str(item) + " was rejected for 3 grouped.")
    for item in delayed_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load3) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load3.append(item)
            delayed_list.remove(item)
        else:
            print(str(item) + " was rejected for 3.")
    for item in truck_list:
        if item in load1 or item in load2 or item in load3:
            deadline_list.remove(item)
        elif len(load3) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This item was found: " + str(item))
            load3.append(item)
            truck_list.remove(item)
        else:
            print(str(item) + " was rejected for 3.")
    for item in free_and_clear_list:
        if item in load1 or item in load2 or item in load3:
            free_and_clear_list.remove(item)
        elif len(load3) < 16 and item not in load1 and item not in load2 and item not in load3:
            print("This free and clear item was found for 3: " + str(item))
            load3.append(item)
            free_and_clear_list.remove(item)
        if len(free_and_clear_list) > 0:
            print("still something there")
        else:
            print("Should be done now")
            break
        break





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
print("This is the free and clear list: " + str(free_and_clear_list) + "\nFree and clear length: " + str(len(free_and_clear_list)))

print("This is the load1 list: " + str(load1) + "\nLoad1 length: " + str(len(load1)))
print("This is the load2 list: " + str(load2) + "\nLoad2 length: " + str(len(load2)))
print("This is the load3 list: " + str(load3) + "\nLoad3 length: " + str(len(load3)))

