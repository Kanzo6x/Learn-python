#LIST

employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}

print(get_employee(12458))



#DICTIONARY

employee_dict = {12345: {"name": "John", "department": "Kitchen"},
                12458: {"name": "Paul", "department": "House Floor"}}

def get_employee_dict(id):
    return employee_dict[12458]

print(get_employee_dict(12458));