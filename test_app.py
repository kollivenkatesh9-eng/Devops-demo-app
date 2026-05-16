employees = [
    {"id": 1, "name": "Teja", "role": "DevOps Engineer"},
    {"id": 2, "name": "Rahul", "role": "Python Developer"},
    {"id": 3, "name": "Anjali", "role": "Cloud Engineer"}
]
 
def test_employee_count():
    assert len(employees) == 3
 
def test_first_employee():
    assert employees[0]["name"] == "Teja"