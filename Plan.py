from Debt import Debt
from Exceptions_primo_pobre import *

class Plan:
    """
    Represents a financial plan containing income, expenses, and debt information.
    The class maintains the state of a financial plan and provides methods to modify its parameters.
    Any modification to the plan's data will mark it as unsolved.
    """

    def __init__(self, plan_name):
        """
        Initializes a new Plan instance with default values.
        """
        self.__plan_name = plan_name

        self.__monthly_available_list = []   ## list of integer values. If there is a value v in the position m, it means that 
                                             ## the person in debt has an ammount v to pay off his or her debts in the month m

        self.__monthly_expenses = 0          ## integer number corresponding to the fixed ammount that is spent monthly
                                             ## This value is deducted from all entries of monthly_available_list

        self.__monthly_incomes = 0           ## integer number corresponding to the fixed ammount that is obtained monthly
                                             ## This value is added to all entries of monthly_available_list
        
        self.__single_income_list = []       ## list of tuple (value, month). It corresponds to an ammount of 'value' that is added to 
                                             ## the value in the position 'month' in the list 'monthly_available_list'

        self.__single_expense_list = []      ## list of tuple (value, month). It corresponds to an ammount of 'value' that is deducted from 
                                             ## the value in the position 'month' in the list 'monthly_available_list'

        self.__plan_duration = 0             ## number of months during which debts can be payed. It is at least 1.
                                             ## If a debt is not completely payed in this interval of time, the problem is not solvable

        self.__debt_dict = { }               ## dictionary of { debt_name : debt_object (Instance of Debt)}

        self.__solution_list = []            ## List with dictionaries in the format {"debt_name" : value_paid}. Completely specifies a solution

        self.__is_solved = None             ## Only true if the current plan has a completely specified solution

        self.__is_duration_set = False       ## Only true if the plan_duration has already been specified

    def copy(self, new_plan_name):
        
        aux = Plan(new_plan_name)
        
        aux.set_plan_duration(self.__plan_duration)
        aux.set_monthly_incomes(self.__monthly_incomes)
        aux.set_monthly_expenses(self.__monthly_expenses)

        for x in self.__single_income_list:
            aux.add_single_income(x[0], x[1])

        for x in self.__single_expense_list:
            aux.add_single_expense(x[0], x[1])

        for x in self.__debt_dict.keys():
            new_debt = self.__debt_dict[x].copy(self.__debt_dict[x].get_name())
            aux.add_debt(new_debt)

        return aux
    
    def get_is_duration_set(self):
        return self.__is_duration_set

    def get_is_solved(self):
        return self.__is_solved
    
    def get_name(self):
        return self.__plan_name
    
    def get_debt (self, debt_name):
        return self.__debt_dict[debt_name]
    
    def get_plan_duration(self):
        return self.__plan_duration

    def get_list_all_debts(self):
        return list( self.__debt_dict.values() )
    
    def get_monthly_incomes(self):
        return self.__monthly_incomes
    
    def get_monthly_expenses(self):
        return self.__monthly_expenses

    def get_single_income_list(self):
        return self.__single_income_list
    
    def get_single_expense_list(self):
        return self.__single_expense_list
    
    def get_monthly_available_list(self):
        return self.__monthly_available_list
    
    def get_solution_list(self):
        return self.__solution_list
    
    def get_debt_dict(self):
        return self.__debt_dict
    
    def get_plan_duration(self):
        return self.__plan_duration
    
    def is_debt_in_the_plan (self, debt_name):
        return debt_name in self.__debt_dict

    def set_solution_list(self, solution_list):
        """
        Calculates and sets the solution list for the plan based on current parameters.
        This method should mark the plan as solved upon successful completion.
        """
        self.__solution_list = solution_list
        
        if  self.__solution_list : 
            self.__is_solved = True

    def print_solution_list(self):
        if(self.__is_solved):
            for entry in self.__solution_list:
                print(entry)
                print("\n")

    def set_plan_duration(self, duration):

        if not self.__is_duration_set:

            if isinstance(duration, int) and duration>0:
                self.__plan_duration = duration
                self.__monthly_available_list = [0 for i in range(0, duration+1)]
                self.__is_duration_set = True
                
            else:
                raise InvalidValue(" duration must be a positive integer.")

        else:
            raise ImproperFunctionUse(" cannot redefine the duration of a plan.")


    def set_monthly_incomes(self, value):

        if self.__is_duration_set:
            if isinstance(value, int) and value>=0:
                self.__monthly_available_list = [self.__monthly_available_list[i] - self.__monthly_incomes for i in range(0, self.__plan_duration+1)]
                self.__monthly_incomes = value
                self.__monthly_available_list = [self.__monthly_available_list[i] + value for i in range(0, self.__plan_duration+1)]
            else:
                raise InvalidValue(" monthly incomes must be a positive integer.")
            
        else:
            raise ImproperFunctionUse(" cannot initialize monthly_incomes without setting a plan duration.")

       

    def set_monthly_expenses(self, value):

        if self.__is_duration_set:

            if isinstance(value, int) and value>=0:

                if value < self.__monthly_incomes:
                    self.__monthly_available_list = [self.__monthly_available_list[i] + self.__monthly_expenses for i in range(0, self.__plan_duration+1)]
                    self.__monthly_expenses = value
                    self.__monthly_available_list = [self.__monthly_available_list[i] - value for i in range(1, self.__plan_duration+1)]
                else: 
                    raise InvalidValue(" monthly expenses value must be at least as large as the monthly incomes.")

            else:
                raise InvalidValue(" monthly expenses value must be a positive integer.")
        
        else:
            raise ImproperFunctionUse(" cannot initialize monthly_expenses without setting a plan duration.")



    def add_single_income(self, value, month):
        
        if self.__is_duration_set:

            if month < self.__plan_duration:

                if isinstance(value, int) and value>=0:
                    self.__monthly_available_list[month] = self.__monthly_available_list[month] + value
                    self.__single_income_list = self.__single_income_list + [ (value, month) ]
                else:
                    raise InvalidValue(" income value must be a positive integer.")
            
            else:
                raise IndexError(" this month is out of the duration specified.")

        else:
            raise ImproperFunctionUse(" cannot add single income without setting a plan duration.")

        

    def add_single_expense(self, value, month):

        if self.__is_duration_set:
            
            if month < self.__plan_duration:

                if isinstance(value, int) and value>=0:

                    if self.__monthly_available_list[month] >= value:
                        self.__monthly_available_list[month] = self.__monthly_available_list[month] - value
                        self.__single_expense_list = self.__single_expense_list + [ (value, month) ]

                    else:
                        raise InvalidValue(" expense value must be at least as large as the monthly available income.")

                else:
                    raise InvalidValue(" expense value must be a positive integer.")
                
            else:
                raise IndexError(" this month is out of the duration specified.")

        else:
            raise ImproperFunctionUse(" cannot add single expense without setting a plan duration.")


    def add_debt(self, debt_name):

        if self.__is_duration_set:

            if not debt_name in self.__debt_dict:
                self.__debt_dict[debt_name] = Debt(debt_name)
            else:
                raise NameError (f" there is already a debt called '{debt_name}' in the plan '{ self.__plan_name }'." )
        
        else:
            raise ImproperFunctionUse(" you cannot add debts without specifying the duration of the plan.")

    def delete_debt(self, debt_name):
        if debt_name in self.__debt_dict:
            del self.__debt_dict[debt_name] 
        else:
            raise NonexistentObject (f' there is no debt called "{debt_name}".')
 

if __name__ == "__main__": ## debugging section
    p = Plan("oss")

    p.set_plan_duration(15)

    p.set_monthly_incomes(100)

    p.set_monthly_expenses(80)

    p.add_single_expense(14, 3)

    p.add_single_expense(1, 2)


