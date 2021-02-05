from FindMissingData import find_missing_data


def two_packages_left(remaining_packages, package_1, package_2, package_3):

    # Initialize counter.
    q = 0

    # Run the same operation used to fill package one, taking into account that package 3's items will
    # remain.
    while q < len(remaining_packages) - 8:
        package_2.append(remaining_packages[q])
        q += 1

    find_missing_data(remaining_packages, package_1, package_2)

    r = 0

    # Remove package_2 items from remaining_packages array.
    while r < len(remaining_packages) - 8:
        remaining_packages.remove(remaining_packages[r])

    # If there are still package data inside the array...
    if len(remaining_packages) >= 1:
        s = 0

        # Add those details to package_3 with same steps as package_1 and package 2.
        while s < len(remaining_packages):
            package_3.append(remaining_packages[s])
            s += 1