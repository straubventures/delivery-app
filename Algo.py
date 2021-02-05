from RecursiveNN import *

def nearest_neighbor(copy_min_table2, load, distances):
    print("\n\n\n")
    print("STARTING A NEW LOAD")
    print("\n\n\n")
    new_load = [[0, "HUB", 1]]
    min_table3 = []
    for list in copy_min_table2:
        min_table3.append(list.copy())

    # The main loop is going through the packages and deciding what to add based on what is closest
    # to that package. However,this does not take into account the most recent package added to new_load.
    # Thus, the primary loop is flawed, and needs to be altered such that it does reflect the most recent package added.

    i = 0
    while i < len(new_load):

        # Create a value list for each package
        value_list = []

        # create a key list for each package
        key_list = []


        # Loop through all the distance lists
        for place, index in enumerate(distances):

            # If the distance list FROM address matches the current package_1 address
            if index[0] == new_load[i][1].lstrip():
                # Capture all the distances for the TO locations

                # Remove any items that have already been added to the new load.
                for item in new_load:
                    if item[1].lstrip() in min_table3[place]:
                        min_table3[place].pop(item[1].lstrip())

                # Capture all distances that lead to the current FROM location
                for each_value in min_table3[place].values():
                    value_list.append(float(each_value))

                # Capture all the addresses for the TO locations
                for each_key in min_table3[place].keys():
                    key_list.append(each_key)

                # Capture the small distance
                mini = min(value_list)

                # Capture the address of the smallest distance
                mini_key = key_list[value_list.index(mini)]
                found = False

                # Loop while we are still searching for a minimum value
                while found is False:

                    if mini_key is None:
                        break

                    # Check if any package in the load has the same address as the min
                    for p2, package in enumerate(load):

                        # If a package's address does match
                        if mini_key == package[1].lstrip():
                            if package not in new_load:
                                found = True
                                # If it is not, then remove it from the load.
                                # and then insert it into the next space after package 1. af
                                new_load.append(package)
                                # Needs to continue so that all packages at the same address are added.
                                continue
                        else: continue
                    if found is False:
                        mini = value_list[key_list.index(mini_key)]
                        mini_key = recursive_checker(mini, mini_key, value_list, key_list, load, new_load)

                        if mini_key is None:
                            break
        i += 1
        continue

    # Indented this forward to actually match the main loop.
    return new_load