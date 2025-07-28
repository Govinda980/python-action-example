def find_max_salary():
    employees = [
        ["A", 90000, "BNG", "IT"],
        ["B", 80000, "HYD", "IT"],
        ["C", 70000, "BNG", "IT"],
        ["D", 100000, "HYD", "IT"],
        ["E", 40000, "HYD", "CS"],
        ["RIYANSH", 400000, "HYD", "CS"]
    ]
    dict_loc_sal = {}
    # Dictionary to store the highest salary per location
    for employee in employees:
        name, salary, location, dept = employee
        if location not in dict_loc_sal or salary > dict_loc_sal[location]:
            dict_loc_sal[location] = salary

    print(dict_loc_sal)


find_max_salary()
