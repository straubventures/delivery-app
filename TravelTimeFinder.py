# add all the traveled miles to the list travel_times so that I can calculate the total travel mileage.
def travel_time_finder(min_graph, load, travel_times):
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



