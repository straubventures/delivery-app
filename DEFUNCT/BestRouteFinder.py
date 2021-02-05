def best_route_finder(load, min_table2, distances):

    use_min_table2 = min_table2
    value_list = []
    key_list = []
    load_list = []

    for p, each_package in enumerate(load):

        for i, index in enumerate(distances):

            if index[0] == each_package[1].lstrip():

                # Get the distance values for this FROM location
                for each_value in use_min_table2[i].values():
                    value_list.append(each_value)

                # Find the min distance
                current_min = min(value_list)

                # Find the min distance index
                min_index = value_list.index(current_min)

                # Find the keys
                for each_value in use_min_table2[i].keys():
                    key_list.append(each_value)

                # Find the key of the min
                current_min_key = key_list[min_index]

                # Check if the min address is in the load
                for the_packages in load:

                    # If you find it, move it to the correct spot.
                    if the_packages[1].lstrip() == current_min_key.lstrip():
                        load_list.insert(p + 1, the_packages)
                        break
                    else:
                        continue

                value_list = []
                key_list = []
    print(" Here is the list " + str(load_list))
    print(len(load_list))
    return load_list

#
    #
    #
    #
    # global key
    # global address
    # for p, each_package in enumerate(load):
    #     for i, index in enumerate(distances):
    #         if index[0] == each_package[1].lstrip():
    #             min_values = use_min_table2[i].values()
    #             keys = use_min_table2[i].keys()
    #             for value in min_values:
    #                 value_list.append(value)
    #
    #             key = value_list.index(min(value_list))
    #             for key1 in keys:
    #                 key_list.append(key1)
    #             address = key_list[key]
    #             for ep, every_package in enumerate(load):
    #                 if distances[key][0] == every_package[1].lstrip():
    #                     load.insert(p + 1, every_package)
    #                     break
    #                 else:
    #                     value_list[key] = 1000
    #                     break
    #
    #     use_min_table2 = min_table2
    #     value_list = []
    #     key_list = []
    #     key = 0
    #     address = ''
    #
    # print(load)
    #
