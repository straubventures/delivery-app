def package_grouper(packages, loads, type_list):
    for each_load in loads:
        if len(each_load) <= (16 - len(packages)):
            for each_package in packages:
                print("hello")
                if each_package[0].lstrip == '39':
                    loads[2].insert(0, each_package)
                elif each_package in each_load:
                    for each_list in type_list:
                        for every_package in each_list:
                            if each_package == every_package:
                                print("found one in the list")
                                each_list.remove(each_package)
                    packages.remove(each_package)
                    for all_others in packages:
                        for every_load in loads:
                            if all_others in every_load:
                                every_load.remove(all_others)
                                for each_list in type_list:
                                    for every_package in each_list:
                                        if each_package == every_package:
                                            print("found one in the list")
                                            each_list.remove(every_package)
                                packages.remove(each_package)
                            else:
                                each_load.append(all_others)
                                continue

                elif len(each_load) < (16 - len(packages)):
                    each_load.append(each_package)
                    for each_list in type_list:
                        if each_package in each_list:
                            each_list.remove(each_package)
                    packages.remove(each_package)
