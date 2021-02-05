def better_nn(distances, load):
    for l, location in enumerate(distances):
        for p, package in enumerate(load):
            min_distance = 0.0
            if package[1].lstrip() == location[0]:
                min_distance = float(min(location))



