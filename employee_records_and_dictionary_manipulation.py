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