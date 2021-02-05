from HashTable import HashTable

# Nearest Neighbor with constraints
from DistancesMatrix import load_distances

# An array of the minimum distance for each location.
min_table = []

# An array of dictionaries that each include the values that are under x miles. The keys are the TO locations.
# The index corresponds with the index of that locations matrix in the distances parameter. Thus, the index can be used
# to identify the FROM location.
min_table2 = []


# Loop through the distances array and
def mind_blowing_algo2(distances):
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
                    # If the distance is less than four miles, add it to the hash-table.
                    if float(j) < 4:
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

    print("\n")

    print(min_table)
    print(min_table2)

    print("\n")
    # The loop below will probably be a separate method

    for z, y in enumerate(min_table2):
        print(min_table2[z])
        print("FROM: " + str(distances[z][0]))
        value_table = min_table2[z].values()
        key_table = min_table2[z].keys()
        key_table2 = []
        value_table2 = []
        for w, x in enumerate(value_table):
            value_table2.append(x)

        # find and print the index of the minimum from the selected hash
        min_index = value_table2.index(min(value_table2))
        print("Minimum Distance: " + str(min(value_table2)))
        print("Minimum Index within Minimum Value List of FROM location: " + str(min_index))

        # list out all the keys from the dictionary and append them to the placeholder list
        for w, x in enumerate(key_table):
            key_table2.append(x)

        # find the key of the minimum from the selected hash using the index found in the above loop
        min_key = key_table2[min_index]
        print("TO: " + str(min_key))
        print(key_table2)
        print(value_table2)
        print("\n")


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


