# Nearest Neighbor with constraints

# Loop through the distances array and
def data_organizer(distances, min_table, min_table2):
    # Fill each array with initial value 10000 (AKA infinity) for the array of minimum distances and
    # empty dictionaries for the array of hash tables which include: the index representing the FROM location,
    # the TO location string as the key, and the distance as the value.
    counter = 0
    while counter <= 26:
        min_table.append(10000)
        min_table2.append({})
        counter += 1

    # Loop through the lists that are pulled from the CSV file.
    for f, i in enumerate(distances):

        # Ignore the first element, which is the HUB.
        if f != 0:

            # Loop through each list within the distances list. This targets the actual distance. Each distance's index
            # consistently corresponds with its address and thus can be used to track which location is selected.
            for l, j in enumerate(i):

                # Ignore the first element of each list, which is the address.
                if l != 0:

                    # If the distance is less than x miles, add it to the hash-table.
                    if float(j) < 13.0:

                        # Add the selected TO location:distance to the hash table of the current FROM location.
                        min_table2[f].__setitem__(distances[l - 1][0], j)

                        # Add the current FROM location:distance to the hash table of the current TO location.
                        min_table2[l - 1].__setitem__(i[0], j)

                    # If the current distance is smaller than the TO location's corresponding index of min_table,
                    # then replace that value with the current one.
                    if float(j) < float(min_table[l - 1]):
                        min_table[l - 1] = float(j)

                    # If the current distance is smaller than the FROM location's corresponding index of the min_table,
                    # then replace that value with the current one.
                    if float(j) < float(min_table[f]):
                        min_table[f] = float(j)

    # The loop below will probably be a separate method

    # Isolate the minimum distance, find the index of the distance within the table, use that index to isolate
    # the address, output the address. Whereas the loop above organizes the data, this series of steps makes use of it
    # by finding the actual minimum values within the filtered hash table of lesser distances. It will enable the
    # easily find the closest distance, and then remove that distance from future options once it is visited.
    for z, y in enumerate(min_table2):

        # Create a view of the distances for the given FROM location.
        value_table = min_table2[z].values()

        # Create a view of the addresses for the given FROM location.
        key_table = min_table2[z].keys()

        # An array that will hold all the addresses of the FROM location, and can be iterated to isolate values.
        key_table2 = []

        # An array that will hold all the distances of the FROM location's filtered choices. The index of each element
        # will then be used to match with the address of the corresponding address in key_table2.
        value_table2 = []

        # Fill value_table2.
        for w, x in enumerate(value_table):
            value_table2.append(x)

        # find and print the index of the minimum distance of the selected FROM location.
        min_index = value_table2.index(min(value_table2))

        # Add all the filtered addresses from the dictionary's view to the array.
        for w, x in enumerate(key_table):
            key_table2.append(x)

        # Find the address of the minimum distance location from the current FROM location via the min
        # distance's value_table2 index.
        min_key = key_table2[min_index]

# The code below details my exploration into Python's dictionary object. While you cannot manipulate data from
# DICT.values, you can iterate through it. This then allowed me to append each data point to an array, from which the
# program could more easily analyze and eventually manipulate the data. This suggests that the full automation of truck
# loading decisions can be achieved.
"""
    # PROOF OF CONCEPT

    # assembles a dict value view
    min_list = min_table2[0].values()
    # assembles a dict keys view
    key_list = min_table2[0].keys()
    # placeholder for min value list
    min_list2 = []
    # placeholder for keys list
    key_list2 = []

    # list out all the values from the dictionary and append them to the placeholder list
    for z, y in enumerate(min_list):
        min_list2.append(y)

    # find the index of the minimum from the selected hash
    print("Print..." + str(min_list2.index('1.9')))

    # list out all the keys from the dictionary and append them to the placeholder list
    for w, x in enumerate(key_list):
        key_list2.append(x)

    # find the key of the minimum from the selected hash using the index found in the above loop
    print("Printing value..." + str(key_list2[3]))

"""


