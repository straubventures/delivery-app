def recursive_checker(mini, mini_key, value_list, key_list, load, new_load):
    found = False

    if mini in value_list:
        value_list.remove(mini)
    if mini_key in key_list:
        key_list.remove(mini_key)

    mini = 100.0
    for value in value_list:
        if float(value) < float(mini):
            mini = float(value)


    # Fixed up the names to be different from the rest of the code
    if mini is not None and mini is not 100.0:

        new_mini_key = key_list[value_list.index(float(mini))]
        return new_mini_key
        # Keep going so you can find other packages with the same address.
        # If there is no matching package, then remove that min value from the list, and check again.