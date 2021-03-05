from Utility import *


# load the critical packages onto the proper loads first.
def prioritize_packages(package, load1, load2, load3,
                        every_package):
    replaced = clean_string(package)

    # Initialize global placeholders for each of the packages that will go to a certain destination.
    package_1 = []
    package_2 = []
    package_3 = []

    all_packages = []

    # This list says that a package is able OK to be loaded onto a certain truck
    inclusive1 = []
    inclusive2 = []
    inclusive3 = []

    loads = [load1, load2, load3]

    def package_adder(a_package):

        inclusive1.append(a_package)
        inclusive2.append(a_package)
        inclusive3.append(a_package)


    # Create an array from the string, replaced. If there are more than 120 characters, there must be more than one
    # package. Therefore, to ensure data is not erased via commas in the comment, reduce the delimiter to 7.
    if len(replaced) <= 160 and replaced.count(',', 0, len(replaced)) < 12:

        # Create array from replaced string.
        package_1 = replaced.split(',', 7)

    # Multiple packages must be present.
    else:
        # Create an array from the string replaced. Lump all excess packages into one element in the last index.
        package_arr = replaced.split(',', 8)

        # If there are package details in package_arr.
        if len(package_arr) >= 2:

            # Counter
            i = 0

            # Loop through package_arr and add each item to package_1, except the last element, which holds all
            # the other packages as one string element.
            while i < len(package_arr) - 1:
                package_1.append(package_arr[i])
                i += 1

            # Initialize new counter.
            j = 0

            # Loop through the array of packages and remove the items that were added to package_1.
            while j < len(package_arr) - 1:
                package_arr.remove(package_arr[j])

            # Create an array out of the remaining package details. Each package should have a length of 8 with
            # comments.
            remaining_packages = package_arr[0].split(',', -1)


            # Check how many packages are left. If there are more than 9 elements, there must be at least 2 more
            # packages.
            if len(remaining_packages) // 8 == 2:

                two_packages_left(remaining_packages, package_1, package_2, package_3)

            # Confirm that there is at least one complete package.
            elif len(remaining_packages) // 8 == 1:

                one_package_left(remaining_packages, package_1, package_2)

    if len(package_1) > 2:
        all_packages.append(package_1)
        every_package.append(package_1)
    if len(package_2) > 2:
        all_packages.append(package_2)
        every_package.append(package_2)
    if len(package_3) > 2:
        all_packages.append(package_3)
        every_package.append(package_3)

    # Loop through the packages inside the local all_packages array, which only includes packages being
    # sent to a single address.
    for package_unit in all_packages:



        # If the package actually exists
        if len(package_unit) > 2:

            if package_unit[7].startswith(" Wrong address"):
                package_unit[1] = ' 410 S State St'
                load3.append(package_unit)
                every_package.remove(package_unit)
                return

            # If the comments section starts with this phrase, then they are added to the "grouped" list.
            elif package_unit[7].startswith(' Must be delivered with'):
                inclusive1.append(package_unit)


            # If the time starts with a 9 or 10, then add them to
            # the global deadline list. These are the only two start hour times included in the sample data.
            elif package_unit[5].startswith('9'):
                inclusive1.append(package_unit)


            elif package_unit[0] == '13' or package_unit[0] == '15' or package_unit[0] == '19' or \
                    package_unit[0] == '14':
                inclusive1.append(package_unit)

            # If the time starts with a 9 or 10, then add them to
            # the global deadline list. These are the only two start hour times included in the sample dat
            elif package_unit[5].startswith(' 10') or package_unit[5].startswith('10'):
                inclusive1.append(package_unit)
                inclusive2.append(package_unit)


            elif package_unit[1].startswith(' 410 S State St'):
                inclusive3.append(package_unit)


            elif package_unit[1].startswith(" 3365") or package_unit[1].startswith(" 2300"):
                inclusive2.append(package_unit)
                inclusive3.append(package_unit)


            elif package_unit[1].startswith(" 355"):
                inclusive3.append(package_unit)

            elif package_unit[1].startswith(" 1060"):
                inclusive3.append(package_unit)

                # Add package to global delayed list if a delay is mentioned in the comments.
            elif package_unit[7].startswith(" Delayed on flight") or package_unit[7].startswith("Delayed on flight"):
                inclusive2.append(package_unit)
                inclusive3.append(package_unit)

            # Add package to trucks list
            elif package_unit[7].startswith(" Can only be"):
                inclusive3.append(package_unit)
                inclusive1.append(package_unit)

            else:
                pass


    if len(package_1) < 2:
        return

# if all the packages filtered through into one of the inclusives, then add them to that load.
    if len(inclusive1) == len(all_packages) and package_1[0] != '28' and len(load1) < 17 - len(all_packages) and len(all_packages) > 1 or package_1[0] == '19' or package_1[0] == '14':
        for each_package in all_packages:
            load1.append(each_package)
            every_package.remove(each_package)

    elif len(inclusive2) == len(all_packages) and len(load2) < 17 - len(all_packages) and len(all_packages) > 1:
        for each_package in all_packages:
            load2.append(each_package)
            every_package.remove(each_package)
        return

    elif package_1[7].lstrip().startswith('Can only') or len(inclusive3) == len(all_packages) and len(load3) < 17 - len(all_packages) and len(all_packages) > 1:
        for each_package in all_packages:
            load3.append(each_package)
            every_package.remove(each_package)
        return
    else:
        pass


















