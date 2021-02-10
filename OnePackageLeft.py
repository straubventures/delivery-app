from FindMissingData import find_missing_data


# When one package is left in the package loader, used for formatting.
def one_package_left(remaining_packages, package_1, package_2):

    find_missing_data(remaining_packages, package_1, package_2)

    # Initialize counter.
    s = 0

    # Add the details to package_2 with same steps as package_1
    while s < len(remaining_packages):
        package_2.append(remaining_packages[s])
        s += 1
