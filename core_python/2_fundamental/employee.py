import abc

class Employee(abc.ABC):

    def __init__(self, fname_val, lname_val):
        self.first_name = fname_val
        self.last_name = lname_val

    # mark as abstract: subclasses must override
    @abc.abstractmethod
    def calculate_paycheck(self):
        raise NotImplementedError("Subclasses must implement calculate_paycheck()")

    # Note: to enforce this at class-creation time, make Employee inherit from abc.ABC
    # and decorate this method with @abc.abstractmethod (requires changing the class header).

class SalaryEmployee(Employee):

    def __init__(self, fname, lname, salary_val):
        super().__init__(fname, lname)
        self.salary = salary_val

    def calculate_paycheck(self):
        return self.salary / 12  # Assuming bi-monthly paychecks
    


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate_val, weekly_hours_val):
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate_val
        self.weekly_hours = weekly_hours_val

    def calculate_paycheck(self):
        return self.hourly_rate * self.weekly_hours
    
class CommissionEmployee(SalaryEmployee):
    """multiple inheritance example: CommissionEmployee inherits from SalaryEmployee"""
    def __init__(self, fname, lname, salary_val, commission_rate_val, sales_amount_val):
        super().__init__(fname, lname, salary_val)
        self.commission_rate = commission_rate_val  # e.g., 0.05 for 5%
        self.sales_amount = sales_amount_val

    def calculate_paycheck(self):
        base_pay = super().calculate_paycheck()
        commission = self.commission_rate * self.sales_amount
        return base_pay + commission