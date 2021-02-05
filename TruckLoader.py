def truck_loader(loads, load, lists, distances, min_table2, speed_list, every_package):
    print('TRUCK LOADER TIME')

    while len(every_package) > 0:

        # Loop through master_type list
        for package_1 in every_package:

            # Loop through all the loads in master_load list
            for load in loads:

                # If the item already exists in any of the loads, remove it.
                if package_1 in load:
                    if package_1 in load:
                        load.remove(package_1)

            # Loop through the loads a second time
            for z, load in enumerate(loads):

                # FROM location goes into the expression
                # miles traveled: min_table2.get("FROM location")
                # TO location: min_table2[i]
                # TODO: Optimize algorithm. Highly inefficient

                # For each list of distances
                for i, j in enumerate(distances):

                    # If the address of the package matches the FROM location on the matrix
                    if j[0] == package_1[1].lstrip():

                        # If the load is not empty
                        if len(loads[0]) + len(loads[1]) + len(loads[2]) < 40 and len(load) < 16:

                            # Loop through the load

                            for y, package_2 in enumerate(load):



                            if min_package is not None and min_package not in load:
                                load.append(min_package)

                                print("I added something here " + str(min_package))

                                if min_package in every_package:
                                    every_package.remove(min_package)
                                    print(str(min_package) + " was magically added and removed from the type_list.")


                    #
                    # If the item is still within the list (because it wasn't removed in the previous loop),
                    # add it to the current load.
                    if item in type_list:
                        if len(load) < 16:
                            print("This item was found: " + str(item))
                            load.append(item)
                            type_list.remove(item)
                            print(str(item) + " was lazily added and removed from the type_list.")
                            break
                        else:
                            print("This load is now full.")
                    else:
                        break



    # # TODO: Can we find packages in the same address that can be added to a load
    # while len(loads[0]) + len(loads[1]) + len(loads[2]) < 40 and len(load) < 16:
    #
    #
    #
    #     for y, package in enumerate(every_package):
    #         for load in loads:
    #             if package in load:
    #                 every_package.remove(package)
    #
    #     # This is the to location
    #     for y, package in enumerate(every_package):
    #         print("NEW PACKAGE")
    #         print('Is this package going into this load?')
    #
    #         min_distance = 90.0
    #         min_keys = None
    #         min_package = None
    #         counter = 1
    #         for load1 in loads:
    #             print("Checking load number " + str(counter))
    #             counter += 1
    #
    #             if load1 == loads[0] and package[7].startswith(' Delayed'):
    #                 print("This package needs to be in a load other than 1")
    #                 continue
    #
    #             if len(loads[0]) + len(loads[1]) + len(loads[2]) < 40 and len(load) < 16:
    #
    #                 for ep, package2 in enumerate(load1):
    #                     print("These are how many miles it takes to travel from " + str(
    #                         package2[1].lstrip()) + " with package id " + package[0].lstrip())
    #                     if len(load1) < 16:
    #                         # Assign the distance-getter to the miles variable
    #                         miles = min_table2[ep + 1].get(package[1].lstrip())
    #
    #                         # Check that there is a distance present and set the
    #                         # maximum allowable distance
    #
    #                         if miles is not None:
    #
    #                             if 0.0 < float(miles) < 20.0:
    #                                 if float(miles) < float(min_distance):
    #                                     print("This is the distance from " + package2[1].lstrip() + ": " + str(miles))
    #
    #                                     for load in loads:
    #                                         if min_package in load and min_package in every_package:
    #                                             every_package.remove(min_package)
    #                                             print("This package is already in the load")
    #                                             continue
    #                                         else:
    #                                             print("Modified the min distance variable")
    #                                             min_distance = miles
    #                                             min_package = package
    #
    #
    #                         print("I added a new min package to this load:" + str(min_package))
    #                     else:
    #                         print("This mileage was too long")
    #             else:
    #                 print('package is already in a load')
    #                 break
    #         else:
    #             print('package has no values')
    #
    #     else:
    #         print("Not good enough")
    #         if min_package is not None:
    #             if min_package not in loads[1] and min_package \
    #                     not in loads[0] and min_package not in loads[2]:
    #                 if float(min_distance) < 20.0:
    #                     load.append(min_package)





