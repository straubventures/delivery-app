# Nathan Straub - ID: 001514364
# I am using the nearest neighbor algorithm, modified with a priority queue based on customer requirements.

from GreedyAlgorithm import greedy_algo
from HashTable import HashTable
from PrioritizePackages import package_loader
from AddRemainingPackages import truck_loader
import csv
from Utility import *
from datetime import *

every_package = []

# Lists of loads
load1 = []
load2 = []
load3 = []

distances = get_distances()
distance_graph = create_graph(distances)
packages = get_packages()


# Add packages to loads based on constraints
z = 0
while z < len(distances):
    package_loader(packages.search(distances[z][0]), load1, load2, load3, every_package)
    z += 1

master_load = [load1, load2, load3]

# add all the remaining packages
truck_loader(master_load, distance_graph, every_package)

# create efficiently navigated paths for each load
new_load1 = greedy_algo(load1, distances)
new_load2 = greedy_algo(load2, distances)
new_load3 = greedy_algo(load3, distances)

# make some adjustments so that the third load can leave on time more consistently.
adjust_paths(new_load1, new_load2, new_load3)

# # Calculate all the travel times
travel_times1 = travel_time_finder(distance_graph, new_load1)
travel_times2 = travel_time_finder(distance_graph, new_load2)
travel_times3 = travel_time_finder(distance_graph, new_load3)

sum1 = find_distance_sum(travel_times1)
sum2 = find_distance_sum(travel_times2)
sum3 = find_distance_sum(travel_times3)

new_master_load = [new_load1, new_load2, new_load3]

# Add delivery status to each item in the load lists.
add_first_status(new_master_load)

all_sum = sum1 + sum2 + sum3
print("The total distance traveled: " + str(all_sum))

# Initiate start times for the trucks
truck2_start = timedelta(0,0,0,0,0,8)
truck1_start = timedelta(0,0,0,0,5,9)
truck3_start = timedelta(0,0,0,0,10,0)

# update the status of each package when they are delivered.
truck2_start = update_delivery_status(travel_times1, truck2_start, new_load1)
truck1_start = update_delivery_status(travel_times2, truck1_start, new_load2)
truck2_start = update_delivery_status(travel_times3, truck2_start, new_load3)

truck_times = [truck1_start, truck2_start, truck3_start]

# add delivery status to hash table.
update_hashtable_delivery_status(master_load, packages)

# create list of ids
master_ids = list_ids(new_master_load)

print('\n')
print("Truck 2 First Load Leaving at 8am " + str(master_ids[0]))
print("Truck 1 First Load Leaving at 9:05am " + str(master_ids[1]))
print("Truck 2 Second Load Leaving Directly after returning from first load: " + str(master_ids[2]))
print('\n')
print("Total Truck 2 Mileage: " + str(sum1 + sum3))
print("Total Truck 1 Mileage: " + str(sum2.__round__(3)))
print('\n')

user_interface(new_master_load, truck_times)