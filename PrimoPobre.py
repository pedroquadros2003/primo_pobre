from Plan import Plan
from Exceptions_primo_pobre import *

class PrimoPobre:
    """
    Class to manage financial plans for dealing with incomes, expenses, and debts.
    Allows creating, copying, deleting, and solving financial plans.
    """

    def __init__(self):
        self.__plan_dict = {}
        self.__plan_solver = 0
        self.__plan_loader = 0
        self.__plan_saver = 0
        self.__plan_stats_maker = 0
        self.__debt_stats_maker = 0

    def create_plan(self, plan_name):
        """
        Creates a new financial plan with the specified name.

        Args:
            plan_name: Name of the plan to be created.

        Raises:
            NameError: This function cannot create a plan with a name already in use.
        """
        if plan_name in self.__plan_dict:
            raise NameError(f"There is already a plan with the name: '{plan_name}'.")
        else:
            self.__plan_dict[plan_name] = Plan(plan_name)

    def copy_plan(self, source_name, target_name):
        """
        Copies an existing plan to a new one with other name.

        Args:
            source_name: Name of the original plan.
            target_name: Name of the new copy.

        Raises: 
            ImproperInput: It cannot copy a plan that does not exist.
            NameError: It does not allow the copy to have a name already in use.
        """
        
        if not source_name in self.__plan_dict:
            raise ImproperInput("The plan you are trying to copy does not exist.")
        else:
            if target_name in self.__plan_dict:
                raise NameError(f"There is already a plan with the name: '{target_name}'.")
            else:
                self.__plan_dict[target_name] = self.__plan_dict[source_name].copy(target_name)


    def delete_plan(self, plan_name):
        """
        Deletes an existing plan.

        Args:
            plan_name: Name of the plan to be deleted.
        
        Raises:
            ImproperFunctionUse: It cannot delete a plan that does not exist.
        """
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to delete does not exist.")
        else:
            del self.__plan_dict[plan_name]

    def list_plans(self): ## it needs improvement
        """
        Lists all existing plans.

        Returns:
            List of all plan names.
        """

        for x in self.__plan_dict.values():
            print(x.get_name())
            print('\n')


    def plan_status(self, plan_name):
        """
        Returns the status of a specific plan.

        Args:
            plan_name: Name of the plan to check.

        Returns:
            Plan status, including incomes, expenses, debts and a solution (if it exists).
        """
        pass

    def save_plan_txt(self, file_name):
        """
        Saves a plan to a text file.

        Args:
            file_name: Name of the file to save to (without extension).
                      The file will be saved as file_name.txt.
        """
        pass

    def load_plan_txt(self, file_name):
        """
        Loads a plan from a text file.

        Args:
            file_name: Name of the file to load.

        Raises:
            ValueError: If a plan with the same name already exists.
        """
        pass

    def solve_plan(self, plan_name):
        """
        Solves a financial plan, considering all debts and available funds.

        Args:
            plan_name: Name of the plan to solve.

        Note:
            If the plan was already solved with no changes, it does nothing.
            Checks debt validity before solving.
        """
        pass

    def set_plan_duration(self, plan_name, duration):
        """
        Sets the duration (in months) of a plan.

        Args:
            plan: Name of the plan.
            duration: Duration in months.

        Raises:
            ImproperFunctionUse: It cannot set the duration of a plan that does not exist.
        """

        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to edit does not exist.")
        else:
            self.__plan_dict[plan_name].set_plan_duration(duration)

        
    def set_monthly_expenses(self, plan_name, value):
        """
        Sets the fixed monthly expenses of a plan.

        Args:
            plan_name: Name of the plan.
            value: Monthly expenses value.

        Raises:
            ImproperFunctionUse: It cannot set the monthly expenses of a plan that does not exist.
        """

        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to edit does not exist.")
        else:
            self.__plan_dict[plan_name].set_monthly_expenses(value)

    def set_monthly_incomes(self, plan_name, value):
        """
        Sets the fixed monthly incomes of a plan.

        Args:
            plan_name: Name of the plan.
            value: Monthly incomes value.

        Raises:
            ImproperFunctionUse: It cannot set the monthly incomes of a plan that does not exist.
        """

        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to edit does not exist.")
        else:
            self.__plan_dict[plan_name].set_monthly_incomes(value)

    def add_single_income(self, plan_name, value, month):
        """
        Adds a one-time income to a specific month.

        Args:
            plan_name: Name of the plan.
            value: Income value.
            month: Target month (1-based index).

        Raises:
            ImproperFunctionUse: It cannot add a single income to a plan that does not exist.
        """
        
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to edit does not exist.")
        else:
            self.__plan_dict[plan_name].add_single_income(plan_name, value, month)
        

    def add_single_expense(self, plan_name, value, month):
        """
        Adds a one-time expense to a specific month.

        Args:
            plan: Name of the plan.
            value: Expense value.
            month: Target month (1-based index).

        Raises:
            ImproperFunctionUse: It cannot add a single expense to a plan that does not exist.
            ImproperFunctionUse: This function cannot deduct more money than what is available to spend in the corresponding month.
        """
        
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan you are trying to edit does not exist.")
        else:
            self.__plan_dict[plan_name].add_single_expense(plan_name, value, month)

    def debt_status(self, debt_name, plan_name):
        """
        Presents the status of a debt.

        Args:
            debt_name: Name of the debt.
            plan_name: Name of the target plan.

        Returns:
            Total to pay, minimum per month, associatede fees and if it is completely specified.
        """

        pass
    

    def add_debt(self, debt_name, plan_name):
        """
        Adds a new debt to a plan.

        Args:
            debt_name: Name of the debt.
            plan_name: Name of the target plan.

        Raises:
            ImproperFunctionUse: It cannot add a debt to a plan that does not exist.
            ImproperInput: It cannot add a debt to a plan in which 'debt_name' is already in use.
        """
        
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("The plan to which you are trying to add a debt does not exist.")
        else:
            self.__plan_dict[plan_name].add_debt(debt_name)


    def delete_debt(self, debt_name, plan_name):
        """
        Removes a debt from a plan.

        Args:
            debt_name: Name of the debt to remove.
            plan_name: Name of the plan.

        Raises:
            ImproperFunctionUse: It cannot delete a debt from a plan that does not exist.
            ImproperInput: It cannot delete a debt which does not exist.
        """
        
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("the plan from which you are trying to delete a debt does not exist.")
        else:
            self.__plan_dict[plan_name].delete_debt(debt_name)

    def set_debt_duration(self, plan_name, debt_name, start, end):
        """
        Sets the duration period for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            start: First month of debt (1-based index).
            end: Last month of debt (1-based index).

        ImproperFunctionUse: It cannot edit a debt from a plan which does not exist.
        ImproperInput: It cannot edit a debt which does not exist.
        """
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("the plan from which you are trying to edit does not exist.")
        else:
            if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
                raise ImproperInput(f'There is no debt called "{debt_name}".')
            else: 
                self.__plan_dict[plan_name].get_debt(debt_name).set_debt_duration(start, end)



    def set_debt_min_per_mth(self, plan_name, debt_name, minimum_per_month):
        """
        Sets the minimum monthly payment for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            minimum_per_month: Minimum payment per month.
        
        Raises:
            ImproperFunctionUse: It cannot edit a debt from a plan which does not exist.
            ImproperInput: It cannot edit a debt which does not exist.
        """
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("the plan from which you are trying to edit does not exist.")
        else:
            if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
                raise ImproperInput(f'There is no debt called "{debt_name}".')
            else: 
                self.__plan_dict[plan_name].get_debt(debt_name).set_debt_min_per_mth(minimum_per_month)


    def set_monthly_fee(self, plan_name, debt_name, monthly_fee):
        """
        Sets the monthly fee percentage for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            monthly_fee: Monthly fee percentage, between 0 and .
        
        Raises:
            ImproperFunctionUse: It cannot edit a debt from a plan which does not exist.
            ImproperInput: It cannot edit a debt which does not exist.
        """
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("the plan from which you are trying to edit does not exist.")
        else:
            if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
                raise ImproperInput(f'There is no debt called "{debt_name}".')
            else: 
                self.__plan_dict[plan_name].get_debt(debt_name).set_monthly_fee(monthly_fee)


    def set_delay_fee(self, plan_name, debt_name, delay_payment_fee):
        """
        Sets the delay payment fee for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            delay_payment_fee: Monthly fee percentage for late payments, between 0 and 100.
                
        Raises:
            ImproperFunctionUse: It cannot edit a debt from a plan which does not exist.
            ImproperInput: It cannot edit a debt which does not exist.
        """
        if not plan_name in self.__plan_dict:
            raise ImproperFunctionUse("the plan from which you are trying to edit does not exist.")
        else:
            if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
                raise ImproperInput(f'There is no debt called "{debt_name}".')
            else: 
                self.__plan_dict[plan_name].get_debt(debt_name).set_monthly_fee(delay_payment_fee)


if __name__ == "__main__":

    primopobre = PrimoPobre()

    primopobre.create_plan("xereca")
    primopobre.create_plan("na_bunda_do_arnobio")
    primopobre.set_plan_duration("xereca", 25)
    primopobre.set_monthly_incomes('xereca', 1200)
    primopobre.set_monthly_expenses('xereca', 200)
    primopobre.add_debt("carro", 'xereca')
    primopobre.set_debt_min_per_mth("xereca", "carro", 200)
    primopobre.set_debt_duration("xereca", "carro", 1, 20)

    primopobre.create_plan("penis")

    primopobre.add_debt("penis", "na_bunda_do_arnobio")
    primopobre.list_plans()



