import csv
from datetime import timedelta

from HashTable import HashTable


def clean_string(package):
    # Parse through unusable package data and turn it into a mutable list.

    replaced = str(package).replace('[', '', -1)
    replaced = str(replaced).replace(']', '', -1)
    replaced = str(replaced).replace('\'', '', -1)

    return replaced


def get_distances():
    # This code reads the distance table, adds the various locations into a HashTable, and then solves the problem.
    data = []
    with open("WGUPS Distance Table clean.csv") as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        for row in read_csv:
            data.append(row)
        return data


def get_packages():
    with open("WGUPS Package File clean.csv", encoding="utf-8-sig") as csv_file2:
        read_csv2 = csv.reader(csv_file2, delimiter=',')
        packages = HashTable()
        for row in read_csv2:
            packages.insert(row)
        return packages


def adjust_paths(new_load1, new_load2, new_load3):
    new_load2.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load2.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load2.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load2.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load2.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load3.append(new_load1[len(new_load1) - 1])
    new_load1.remove(new_load1[len(new_load1) - 1])

    new_load1.append(new_load3[2])
    new_load3.remove(new_load3[2])

    new_load1.append(new_load3[1])
    new_load3.remove(new_load3[1])

    new_load2.insert(1, new_load1[6])
    new_load1.remove(new_load1[6])

    packs = new_load2[8]
    new_load2.remove(new_load2[8])
    new_load2.insert(1, packs)


def find_distance_sum(travel_times):
    sum = 0.0
    for distance in travel_times:
        sum += float(distance)
    return sum


def update_hashtable_delivery_status(master_load, packages):
    for load in master_load:
        packages.insert_delivery_status(load)


def list_ids(new_master_load):
    load1_ids = []
    load2_ids = []
    load3_ids = []
    for i, load in enumerate(new_master_load):
        for package in load:
            if package[0] == 0:
                continue
            elif i == 0:
                load1_ids.append(package[0].lstrip())
            elif i == 1:
                load2_ids.append(package[0].lstrip())
            elif i == 2:
                load3_ids.append(package[0].lstrip())
    master_ids = [load1_ids, load2_ids, load3_ids]
    return master_ids


def update_delivery_status(travel_time, truck_start, load):
    for i, time in enumerate(travel_time):
        truck_start += timedelta(0, 0, 0, 0, 0, (float(float(travel_time[i]) / 18)))
        if time is not None:
            if len(load[i]) > 4:
                load[i][8] = "Delivered"
                load[i].append(truck_start)
    return truck_start



def add_first_status(new_master_load):
    for truckload in new_master_load:
        for package in truckload:
            package.append("At Hub")

def user_interface(new_master_load, truck_times):
    # User interface
    while 0 < 1:
        report = input("Type the package ID you wish to check on or type 'all' to view all packages: ")
        if report == 'exit':
            exit(0)
        elif report == 'all':
            for i, load in enumerate(new_master_load):
                for package in load:
                    if len(package) > 4:
                        if i == 0:
                            print("Package-ID " + str(package[0].lstrip()) + " was delivered at " + str(
                                str(package[9])) + " on truck 2 in load 1.")
                        elif i == 1:
                            print("Package-ID " + str(package[0].lstrip()) + " was delivered at " + str(
                                str(package[9])) + " on truck 1 in load 2.")
                        elif i == 2:
                            print("Package-ID " + str(package[0].lstrip()) + " was delivered at " + str(
                                str(package[9])) + " on truck 2 in load 3.")
        elif report == 'time1':
            for i, load in enumerate(new_master_load):
                for package in load:
                    truck_num = ''
                    if (i + 1) / 2 == 1:
                        truck_num = '1'
                    else:
                        truck_num = '2'
                    if len(package) > 4:
                        requested_time = timedelta(0, 0, 0, 0, 40, 12).seconds
                        if truck_times[i].seconds < requested_time < package[9].seconds:
                            print("Package-ID " + str(package[0].lstrip()) + " is en route on truck " + truck_num)
                        elif requested_time > package[9].seconds:
                            print("Package-ID " + str(package[0].lstrip()) + " was delivered at " + str(
                                package[9]) + " by truck " + truck_num)
                        else:
                            print("Package-ID " + str(package[0].lstrip()) + " is waiting at the Hub.")
        else:
            for lo, load in enumerate(new_master_load):
                for p, package in enumerate(load):
                    if (lo + 1) / 2 == 1:
                        truck_num = 1
                    else:
                        truck_num = 0
                    if str(package[0]).lstrip() == report:
                        print(package)
                        hour = input("For what time would you like this package's status? Please type the hour first: ")
                        minute = input("And now the minutes: ")
                        requested_time = timedelta(0, 0, 0, 0, int(minute), int(hour)).seconds
                        if truck_times[truck_num].seconds < requested_time < package[9].seconds:
                            print("Package is en route at " + str(hour) + ":" + str(minute))
                            break
                        elif requested_time > package[9].seconds:
                            print("Package was delivered at " + str(package[9]))
                            break
                        else:
                            print("Package is at the Hub at " + str(hour) + ":" + str(minute))
                            break


                    else:
                        continue


# create a dictionary of dictionaries for the location data
def create_graph(distance_table):
    empty_dict = {}
    for loc in distance_table:
        address = loc[0]
        empty_dict.__setitem__(address, {})

    for f, i in enumerate(distance_table):

        for l, j in enumerate(i):

            # Skip zero since it's the address
            if l != 0:

                # Add the selected TO location:distance to the hash table of the current FROM location.
                empty_dict[i[0]].__setitem__(distance_table[l - 1][0], j)

                # Add the current FROM location:distance to the hash table of the current TO location.
                empty_dict[distance_table[l - 1][0]].__setitem__(i[0], j)

    return empty_dict


def find_missing_data(source, package1, package2):
    # Check if a "Delivered with" package ID was mis-identified as a separate element.
    if len(package2) > 8:

        # Assign erroneous element to readable variable.
        error_final_el = package2[len(package2) - 1].replace(' ', '')

        # Assign proper final element to readable variable
        proper_final_el = package2[len(package2) - 2]

        # Check if the last element is a number. If yes, join that element with the prior one.
        if error_final_el.isnumeric():

            package2[len(package2) - 2] = proper_final_el.join([proper_final_el + ", " + str(error_final_el)])
            package2.remove(package2[len(package2) - 1])

    # Check if a "Delivered with" package ID was mis-identified as a separate element for package_1.
    elif len(source[0]) <= 3 and len(source[1]) <= 3:

        # Assign erroneous element to readable variable.
        error_final_el = source[0].replace(' ', '')

        # Assign proper final element to readable variable
        proper_final_el = package1[len(package1) - 1]

        # Check if the last element is a number. If yes, join that element with the prior one.
        if error_final_el.isnumeric():

            package1[len(package1) - 1] = proper_final_el.join([proper_final_el + ", " + str(error_final_el)])
            source.remove(source[0])


# erase the minimum value provided in the value list and find the new min, then return the new min key.
def find_next_min(mini, mini_key, value_list, key_list, load, new_load):
    found = False

    if mini in value_list:
        value_list.remove(mini)
    if mini_key in key_list:
        key_list.remove(mini_key)

    mini = 100.0
    for value in value_list:
        if mini is None:
            continue
        if float(value) < float(mini):
            mini = float(value)


    # Fixed up the names to be different from the rest of the code
    if mini is not None and mini != 100.0:

        new_mini_key = key_list[value_list.index(float(mini))]
        return new_mini_key
        # Keep going so you can find other packages with the same address.
        # If there is no matching package, then remove that min value from the list, and check again.


# When one package is left in the package loader, used for formatting.
def one_package_left(remaining_packages, package_1, package_2):

    find_missing_data(remaining_packages, package_1, package_2)

    # Initialize counter.
    s = 0

    # Add the details to package_2 with same steps as package_1
    while s < len(remaining_packages):
        package_2.append(remaining_packages[s])
        s += 1


# Formatter used in package loader when there are two packages remaining.
def two_packages_left(remaining_packages, package_1, package_2, package_3):

    # Initialize counter.
    q = 0

    # Run the same operation used to fill package one, taking into account that package 3's items will
    # remain.
    while q < len(remaining_packages) - 8:
        package_2.append(remaining_packages[q])
        q += 1

    find_missing_data(remaining_packages, package_1, package_2)

    r = 0

    # Remove package_2 items from remaining_packages array.
    while r < len(remaining_packages) - 8:
        remaining_packages.remove(remaining_packages[r])

    # If there are still package data inTside the array...
    if len(remaining_packages) >= 1:
        s = 0

        # Add those details to package_3 with same steps as package_1 and package 2.
        while s < len(remaining_packages):
            package_3.append(remaining_packages[s])
            s += 1


# add all the traveled miles to the list travel_times so that I can calculate the total travel mileage.
def travel_time_finder(min_graph, load):
    travel_times = []
    # Loop through all the packages
    the_time = 0


    for i, package in enumerate(load):
        if i < len(load) - 1:
            from_location = package[1].lstrip()
            to_location = load[i + 1][1].lstrip()
            travel_times.append(min_graph.get(from_location).get(to_location))
            the_time = the_time + (float(min_graph.get(from_location).get(to_location)) / 18.0)

        else:
            travel_times.append(min_graph["HUB"].get(load[i][1].lstrip()))
            the_time = the_time + (float(min_graph["HUB"].get(load[i][1].lstrip())) / 18.0)
    return travel_times



