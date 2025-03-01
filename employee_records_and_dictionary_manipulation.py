company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print("Initial company employees:")
print(company_employees)

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print("\nAfter adding David:")
print(company_employees)

def count_employees(company):
    total = 0
    for department in company.values():
        total += len(department)
    return total

print("\nTotal number of employees:", count_employees(company_employees))

def transform_dictionary(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if value not in output_dict:
            output_dict[value] = []
        output_dict[value].append(key)
    return output_dict


input_dict = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
output_dict = transform_dictionary(input_dict)
print("\nTransformed dictionary:")
print(output_dict)

company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}


print("Initial company employees:")
print(company_employees)


company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print("\nAfter adding David:")
print(company_employees)


def count_employees(company):
    total = 0
    for department in company.values():
        total += len(department)
    return total


print("\nTotal number of employees:", count_employees(company_employees))

def transform_dictionary(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if value not in output_dict:
            output_dict[value] = []
        output_dict[value].append(key)
    return output_dict


input_dict = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
output_dict = transform_dictionary(input_dict)
print("\nTransformed dictionary:")
print(output_dict)