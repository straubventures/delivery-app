import csv

# create a dictionary of dictionaries for the location data
def create_graph(distance_table, empty_dict):

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

