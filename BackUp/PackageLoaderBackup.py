def package_loader(package):
    # Parse through unusable package data and turn it into a mutable list.
    print('\n')
    replaced = str(package).replace('[', '', -1)
    replaced = str(replaced).replace(']', '', -1)
    replaced = str(replaced).replace('\'', '', -1)
    print('\n')

    # Print the current form of replaced
    print("This is the current form of replaced: " + str(replaced))

    # Initialize global placeholders for each of the packages that will go to a certain destination.
    package_1 = []
    package_2 = []
    package_3 = []

    # Create an array from the string, replaced. If there are more than 120 characters, there must be more than one
    # package. Therefore, to ensure data is not erased via commas in the comment, reduce the delimiter to 7.
    if len(replaced) <= 120 and replaced.count(',', 0, len(replaced)) < 12:

        # Print confirmation that this step took place
        print("Single package or none identified.")

        # Create array from replaced string.
        package_1 = replaced.split(',', 7)
        print("This is package_1: " + str(package_1))

    # Multiple packages must be present.
    else:

        # Print declaration that multiple packages have been detected.
        print("Multiple packages have been detected.")

        # Create an array from the string replaced. Lump all excess packages into one element in the last index.
        package_arr = replaced.split(',', 8)

        # If there are package details in package_arr.
        if len(package_arr) >= 2:

            # Print the contents of package_arr for later testing.
            print("This is the original package_arr: " + str(package_arr))

            # Counter
            i = 0

            # Loop through package_arr and add each item to package_1, except the last element, which holds all
            # the other packages as one string element.
            while i < len(package_arr) - 1:
                package_1.append(package_arr[i])
                i += 1
                # TODO add a validation for commas inside the comment element so that data is not lost.

            # Initialize new counter.
            j = 0

            # Loop through the array of packages and remove the items that were added to package_1.
            while j < len(package_arr) - 1:
                package_arr.remove(package_arr[j])

            # Confirm that package_1 was properly identified.
            print("This is package 1 " + str(package_1))

            # Create an array out of the remaining package details. Each package should have a length of 8 with
            # comments.
            remaining_packages = package_arr[0].split(',', -1)

            # Print the remaining package details.
            print("These are the remaining package details: " + str(remaining_packages))

            # Check how many packages are left. If there are more than 9 elements, there must be at least 2 more
            # packages.
            if len(remaining_packages) // 8 == 2:

                number_of_remaining_packages = len(remaining_packages) // 8

                # Print confirmation there are 2 more packages left.
                print(
                    "The program detects " + str(number_of_remaining_packages) + " more package(s) for this location.")

                # Initialize counter.
                q = 0

                # Run the same operation used to fill package one, taking into account that package 3's items will
                # remain.
                while q < len(remaining_packages) - 8:
                    package_2.append(remaining_packages[q])
                    q += 1

                # Check if a "Delivered with" package ID was mis-identified as a separate element.
                if len(package_2) > 8:

                    # Print confirmation that package 2 was identified as too long.
                    print("Package 2 is too long")

                    # Assign erroneous element to readable variable.
                    error_final_el = package_2[len(package_2) - 1].replace(' ', '')

                    # Assign proper final element to readable variable
                    proper_final_el = package_2[len(package_2) - 2]

                    # Check if the last element is a number. If yes, join that element with the prior one.
                    if error_final_el.isnumeric():
                        # Print confirmation that a number was identified.
                        print("A number was found in package_2's erroneous element.")

                        package_2[len(package_2) - 2] = proper_final_el.join(
                            [proper_final_el + ", " + str(error_final_el)])
                        package_2.remove(package_2[len(package_2) - 1])

                # Check if a "Delivered with" package ID was mis-identified as a separate element for package_1.
                elif len(remaining_packages[0]) <= 3 and len(remaining_packages[1]) <= 3:

                    # Print confirmation that package 2 was identified as too long.
                    print("Package 1 is missing date")

                    # Assign erroneous element to readable variable.
                    error_final_el = remaining_packages[0].replace(' ', '')

                    # Assign proper final element to readable variable
                    proper_final_el = package_1[len(package_1) - 1]

                    # Check if the last element is a number. If yes, join that element with the prior one.
                    if error_final_el.isnumeric():
                        # Print confirmation that a number was identified.
                        print("A number was found in package_2's erroneous element.")

                        package_1[len(package_1) - 1] = proper_final_el.join(
                            [proper_final_el + ", " + str(error_final_el)])
                        remaining_packages.remove(remaining_packages[0])

                # Confirm that package_2 filled properly.
                print("This is package_2: " + str(package_2))
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

                    # Confirm that package_3 was found successfully.
                    print("This is package_3: " + str(package_3))

            # Confirm that there is at least one complete package.
            elif len(remaining_packages) // 8 == 1:

                # Print the number of packages remaining
                print("The program detects " + str(len(remaining_packages) // 8) + " package(s) remaining.")

                print("The remaining package data is: " + str(remaining_packages))

                # Check if a "Delivered with" package ID was mis-identified as a separate element.
                if len(package_2) > 8:

                    # Print confirmation that package 2 was identified as too long.
                    print("Package 2 is too long")

                    # Assign erroneous element to readable variable.
                    error_final_el = package_2[len(package_2) - 1].replace(' ', '')

                    # Assign proper final element to readable variable
                    proper_final_el = package_2[len(package_2) - 2]

                    # Check if the last element is a number. If yes, join that element with the prior one.
                    if error_final_el.isnumeric():
                        # Print confirmation that a number was identified.
                        print("A number was found in package_2's erroneous element.")

                        package_2[len(package_2) - 2] = proper_final_el.join(
                            [proper_final_el + ", " + str(error_final_el)])
                        package_2.remove(package_2[len(package_2) - 1])

                # Check if a "Delivered with" package ID was mis-identified as a separate element for package_1.
                elif len(remaining_packages[0]) <= 3 and len(remaining_packages[1]) <= 3:

                    # Print confirmation that package 2 was identified as too long.
                    print("Package 1 is missing date")

                    # Assign erroneous element to readable variable.
                    error_final_el = remaining_packages[0].replace(' ', '')

                    # Assign proper final element to readable variable
                    proper_final_el = package_1[len(package_1) - 1]

                    # Check if the last element is a number. If yes, join that element with the prior one.
                    if error_final_el.isnumeric():
                        # Print confirmation that a number was identified.
                        print("A number was found in package_1's erroneous element.")

                        package_1[len(package_1) - 1] = str(proper_final_el) + ", " + str(error_final_el)

                        # Print confirmation that the final value of package_1 was updated.
                        print("Updated package_1: " + str(package_1))

                        remaining_packages.remove(remaining_packages[0])

                # Initialize counter.
                s = 0

                # Add the details to package_2 with same steps as package_1
                while s < len(remaining_packages):
                    package_2.append(remaining_packages[s])
                    s += 1
                print("This is package_2: " + str(package_2))




