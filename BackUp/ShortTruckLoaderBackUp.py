def truck_loader(loads, load, lists):

    while len(load) < 16:

        # Loop through master_type list
        for type_list in lists:

            # Loop through each item in each list
            for item in type_list:

                # Loop through all the loads in master_load list
                for load in loads:

                    # If the item already exists in any of the loads, remove it.
                    if item in load:
                        type_list.remove(item)
                        print(str(item) + " was found in a load already, so it was removed from list.")
                        break

                # Loop through the loads a second time
                for load in loads:

                    # If the item is still within the list (because it wasn't removed in the previous loop),
                    # add it to the current load.
                    if item in type_list:
                        if len(load) < 16:
                            print("This item was found: " + str(item))
                            load.append(item)
                            type_list.remove(item)
                            print(str(item) + " was added and removed from the type_list.")
                            break
                        else:
                            print("This load is now full.")
                    else:
                        break


