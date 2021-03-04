from Utility import create_graph, find_next_min


def greedy_algo(load, distances):

    new_load = [[0, "HUB", 1]]

    # create new graph that can be used without altering the actual location data structure
    copy_min_graph = create_graph(distances)


    i = 0
    while i < len(load):

        # Create a value list for each package
        value_list = []

        # create a key list for each package
        key_list = []


        # Loop through all the distance lists
        for place, index in enumerate(new_load):

            if place == len(new_load) - 1:

                # Capture all the distances for the TO locations
                from_location = copy_min_graph[index[1].lstrip()]
                # Remove any items that have already been added to the new load.
                for item in new_load:
                    to_location = item[1].lstrip()
                    if to_location in from_location:
                        from_location.pop(to_location)

                # Capture all distances that lead to the current FROM location
                for each_value in from_location.values():
                    value_list.append(float(each_value))

                # Capture all the addresses for the TO locations
                for each_key in from_location.keys():
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
                        mini_key = find_next_min(mini, mini_key, value_list, key_list, load, new_load)

                        if mini_key is None:
                            break
        i = len(new_load)
        continue

    # prioritize deadline packages by moving them to the front of the load.
    for item in new_load:
        if len(item) > 4:
            if item[5].lstrip().startswith("10") or item[5].lstrip().startswith("9"):
                new_load.remove(item)
                new_load.insert(1, item)
                for item_2 in new_load:
                    if item_2[1] == item[1]:
                        new_load.remove(item_2)
                        new_load.insert(1, item_2)


    return new_load