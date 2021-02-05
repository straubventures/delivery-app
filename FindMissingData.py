def find_missing_data(source, package1, package2):
    # Check if a "Delivered with" package ID was mis-identified as a separate element.
    if len(package2) > 8:

        # Assign erroneous element to readable variable.
        error_final_el = package2[len(package2) - 1].replace(' ', '')

        # Assign proper final element to readable variable
        proper_final_el = package2[len(package2) - 2]

        # Check if the last element is a number. If yes, join that element with the prior one.
        if error_final_el.isnumeric():

            package2[len(package2) - 2] = proper_final_el.join([proper_final_el + ", " + str(error_final_el)])
            package2.remove(package2[len(package2) - 1])

    # Check if a "Delivered with" package ID was mis-identified as a separate element for package_1.
    elif len(source[0]) <= 3 and len(source[1]) <= 3:

        # Assign erroneous element to readable variable.
        error_final_el = source[0].replace(' ', '')

        # Assign proper final element to readable variable
        proper_final_el = package1[len(package1) - 1]

        # Check if the last element is a number. If yes, join that element with the prior one.
        if error_final_el.isnumeric():

            package1[len(package1) - 1] = proper_final_el.join([proper_final_el + ", " + str(error_final_el)])
            source.remove(source[0])