def travel_time_finder(min_table2, distances, load, travel_times):
    # Loop through all the packages
    for i, unit in enumerate(load):

        # Loop through the distance matrix
        for k, address_hub in enumerate(distances):

            # If the load has enough capacity
            if len(load) > i + 1:
                # Check if the address of the TO location  in the hub
                # matches the address of the package
                if address_hub[0] == load[i][1].lstrip():
                    # if min_table2[k].get(load[i + 1][1].lstrip()) is not None:
                    if min_table2[k].get(load[i + 1][1].lstrip()) is not None:
                        # Add the travel time FROM the current location TO the next location into the travel_times list
                        travel_times.append(float(min_table2[k].get(load[i + 1][1].lstrip())))
                    else:
                        travel_times.append(0.0)

                # If the address is not a match, then keep going forward in the loop
                else:
                    continue

    # if this is the last index
    travel_times.append(min_table2[0].get(load[len(load) - 1][1].lstrip()))
