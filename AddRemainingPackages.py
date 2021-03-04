
# Fill in the remaining gaps in the loads with the rest of the packages.
def truck_loader(loads, min_graph, every_package):
    while len(every_package) > 0:
        for package in every_package:
            min_distance = 1000
            min_coordinate = None
            finder_package = None
            for j, load in enumerate(loads):
                if len(load) < 16:
                    for i, loaded_package in enumerate(load):
                        if package not in every_package:
                            break
                        if len(every_package) == 0:
                            return
                        if len(load) < 16:
                            if j % 3 == 0 and package[7].lstrip().startswith('Delayed'):
                                continue

                            # from_location = min_graph.get(package[1].lstrip())
                            # to_location = loaded_package[1].lstrip()


                            if float(min_graph.get(package[1].lstrip()).get(loaded_package[1].lstrip())) < min_distance:
                                min_distance = float(min_graph.get(package[1].lstrip()).get(loaded_package[1].lstrip()))
                                finder_package = loaded_package
                                min_coordinate = i + 1

            for load in loads:
                if finder_package in load:

                    load.insert(min_coordinate, package)

                    every_package.remove(package)
                    if every_package == 0:
                        return
                else:
                    continue
