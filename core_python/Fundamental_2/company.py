from typing import List
from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(f"{emp.first_name} {emp.last_name}: ${emp.calculate_paycheck():,.2f}")
        print("-----------------------------------------------")


def main():
    my_company = Company()
    emp1 = SalaryEmployee("John", "Doe", 60000)
    emp2 = HourlyEmployee("Jane", "Smith", 25, 40)
    emp3 = CommissionEmployee("Alice", "Johnson", 50000, 0.10, 20000)
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    my_company.add_employee(emp3)

    print("\n".join([f"{emp.first_name} {emp.last_name}: ${emp.calculate_paycheck():,.2f}" for emp in my_company.employees]))

def take_a_list(lst: List[int]) -> None:
    pass
if __name__ == "__main__":
    main()