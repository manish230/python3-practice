employee1 = {
    "name": "manish", 
    "age": 29,
    "position": "developer",
    "salary": 1400
}
employee2 = {
    "name": "manoj", 
    "age": 31,
    "position": "tester",
    "salary": 1200
}


def increaase_salary(employee, percent):
     employee['salary'] += employee['salary'] * (percent/100)

employees = [employee1, employee2]

for employee in employees:
    print(f"{employee["name"]} salary  is ${employee["salary"]}")

new_salalry = increaase_salary(employee1, 20)
print(f"{employee1["salary"]}")
