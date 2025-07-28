employees = [
    ["A", 90000, "BNG", "IT"],
    ["B", 80000, "HYD", "IT"],
    ["C", 70000, "BNG", "IT"],
    ["D", 100000, "HYD", "IT"],
    ["E", 40000, "HYD", "CS"],
    ["RIYANSH", 400000, "HYD", "CS"],
    ["Govinda", 800000, "HYD", "CS"]

]


def find_highest_salary_location_wise():
    dict_max_loc = {}
    for employee in employees:
        name, salary, location, dept = employee
        if location not in dict_max_loc or salary > dict_max_loc[location]:
            dict_max_loc[location] = salary
    print(dict_max_loc)


def get_max_salary_among_all_dept():
    dict_max_loc = {}
    for employee in employees:
        name, salary, location, dept = employee
        if location not in dict_max_loc or salary > dict_max_loc[location]:
            dict_max_loc[location] = salary
    # sorted_dic = dict(sorted(dict_max_loc.items(), key=lambda dict_max_loc: dict_max_loc[1]))

    max_val = max(dict_max_loc.items(), key=lambda dict_max: dict_max[1])

    print(max_val)


if __name__ == '__main__':
    find_highest_salary_location_wise()
    get_max_salary_among_all_dept()
