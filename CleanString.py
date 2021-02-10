def clean_string(package):
    # Parse through unusable package data and turn it into a mutable list.

    replaced = str(package).replace('[', '', -1)
    replaced = str(replaced).replace(']', '', -1)
    replaced = str(replaced).replace('\'', '', -1)

    return replaced
