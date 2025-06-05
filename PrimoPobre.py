from Plan import Plan
from Debt import Debt
from Exceptions_primo_pobre import *
from PlanSaver import PlanSaver
from PlanLoader import PlanLoader
from PlanSolver import PlanSolver
from PlanStatsMaker import PlanStatsMaker

class PrimoPobre:
    """
    Class to manage financial plans for dealing with incomes, expenses, and debts.
    Allows creating, copying, deleting, and solving financial plans.
    """

    def __init__(self):
        self.__plan_dict = {}
        self.__plan_solver = PlanSolver()
        self.__plan_loader = PlanLoader()
        self.__plan_saver = PlanSaver()
        self.__plan_stats_maker = PlanStatsMaker()
        self.__debt_stats_maker = 0

    def create_plan(self, plan_name):
        """
        Creates a new financial plan with the specified name.

        Args:
            plan_name: Name of the plan to be created.

        Raises:
            NameError: It cannot create a plan with a name already in use.
        """
        if plan_name in self.__plan_dict.keys():
            raise NameError(f" there is already a plan with the name: '{plan_name}'.")
        else:
            self.__plan_dict[plan_name] = Plan(plan_name)

    def copy_plan(self, source_name, target_name):
        """
        Copies an existing plan to a new one with other name.

        Args:
            source_name: Name of the original plan.
            target_name: Name of the new copy.

        Raises: 
            NonexistentObject: It cannot copy a plan that does not exist.
            NameError: It does not allow the copy to have a name already in use.
        """
        if not source_name in self.__plan_dict:
            raise NonexistentObject(" the plan you are trying to copy does not exist.")
        else:
            if target_name in self.__plan_dict:
                raise NameError(f" there is already a plan with the name: '{target_name}'.")
            else:
                self.__plan_dict[target_name] = self.__plan_dict[source_name].copy(target_name)

    def delete_plan(self, plan_name):
        """
        Deletes an existing plan.

        Args:
            plan_name: Name of the plan to be deleted.
        
        Raises:
            NonexistentObject: It cannot delete a plan that does not exist.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to delete does not exist.")
        else:
            del self.__plan_dict[plan_name]

    def list_plans(self):
        """
        Lists all existing plans.

        Returns:
            List of all plan names.
        """
        print("Current plans are: ")
        for x in self.__plan_dict.values():
            print(f'   -> {x.get_name()}')

    def plan_status(self, plan_name):
        """
        Returns the status of a specific plan.

        Args:
            plan_name: Name of the plan to check.

        Returns:
            Plan status, including incomes, expenses, debts and a solution.
             
        Raises:
            NonexistentObject: It cannot return the status of an unexisting plan.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to check does not exist.")
        return self.__plan_dict[plan_name]

    def save_plan_txt(self, file_name, plan_name):
        """
        Saves a plan to a text file.

        Args:
            file_name: Name of the file to save to (without extension).
                      The file will be saved as file_name.txt.
            plan_name: Name of the plan to save.
        
        Raises:
            NonexistentObject: It cannot save an unexisting plan.
            ValueError: If there's an error saving the file.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to save does not exist.")
        try:
            self.__plan_saver.save_plan_txt(file_name, self.__plan_dict[plan_name])
        except Exception as e:
            raise ValueError(f"Error saving plan: {str(e)}")

    def load_plan_txt(self, file_name):
        """
        Loads a plan from a text file.

        Args:
            file_name: Name of the file to load.

        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            ValueError: If the file format is invalid.
            NameError: If a plan with the same name already exists.
        """
        try:
            plan = self.__plan_loader.load_plan_txt(file_name)
            if plan.get_name() in self.__plan_dict:
                raise NameError(f" there is already a plan with the name: '{plan.get_name()}'.")
            self.__plan_dict[plan.get_name()] = plan
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e))
        except Exception as e:
            raise ValueError(f"Error loading plan: {str(e)}")

    def solve_plan(self, plan_name):
        """
        Solves a financial plan, considering all debts and available funds.

        Args:
            plan_name: Name of the plan to solve.

        Raises:
            NonexistentObject: It cannot solve a plan that does not exist.
            NotCompletelySpecified: There is not sufficient information regarding the plan and its debts.
            WronglySpecified: There are debts which are due to months ahead the duration of the plan.    
        
        Note:
            If the plan was already solved with no changes, it does nothing.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to solve does not exist.")
        self.__plan_solver.solve(self.__plan_dict[plan_name])

    def set_plan_duration(self, plan_name, duration):
        """
        Sets the duration (in months) of a plan.

        Args:
            plan_name: Name of the plan.
            duration: Duration in months.

        Raises:
            NonexistentObject: It cannot set the duration of a plan that does not exist.
            InvalidValue: Duration must be a positive integer.
            ImproperFunctionUse: Cannot redefine the duration of a plan.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to edit does not exist.")
        self.__plan_dict[plan_name].set_plan_duration(duration)

    def set_monthly_expenses(self, plan_name, value):
        """
        Sets the fixed monthly expenses of a plan.

        Args:
            plan_name: Name of the plan.
            value: Monthly expenses value.

        Raises:
            NonexistentObject: It cannot set the monthly expenses of a plan that does not exist.
            InvalidValue: Monthly expenses must be a positive integer and less than monthly incomes.
            ImproperFunctionUse: Cannot set expenses without setting plan duration first.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to edit does not exist.")
        self.__plan_dict[plan_name].set_monthly_expenses(value)

    def set_monthly_incomes(self, plan_name, value):
        """
        Sets the fixed monthly incomes of a plan.

        Args:
            plan_name: Name of the plan.
            value: Monthly incomes value.

        Raises:
            NonexistentObject: It cannot set the monthly incomes of a plan that does not exist.
            InvalidValue: Monthly incomes must be a positive integer.
            ImproperFunctionUse: Cannot set incomes without setting plan duration first.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to edit does not exist.")
        self.__plan_dict[plan_name].set_monthly_incomes(value)

    def add_single_income(self, plan_name, value, month):
        """
        Adds a one-time income to a specific month.

        Args:
            plan_name: Name of the plan.
            value: Income value.
            month: Target month (1-based index).

        Raises:
            NonexistentObject: It cannot add a single income to a plan that does not exist.
            InvalidValue: Income value must be a positive integer.
            IndexError: Month is out of the plan duration.
            ImproperFunctionUse: Cannot add income without setting plan duration first.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to edit does not exist.")
        self.__plan_dict[plan_name].add_single_income(value, month)

    def add_single_expense(self, plan_name, value, month):
        """
        Adds a one-time expense to a specific month.

        Args:
            plan_name: Name of the plan.
            value: Expense value.
            month: Target month (1-based index).

        Raises:
            NonexistentObject: It cannot add a single expense to a plan that does not exist.
            InvalidValue: Expense value must be a positive integer and not exceed available funds.
            IndexError: Month is out of the plan duration.
            ImproperFunctionUse: Cannot add expense without setting plan duration first.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan you are trying to edit does not exist.")
        self.__plan_dict[plan_name].add_single_expense(value, month)

    def add_debt(self, plan_name, debt_name):
        """
        Adds a new debt to a plan.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.

        Raises:
            NonexistentObject: It cannot add a debt to a plan that does not exist.
            NameError: It cannot add a debt to a plan in which 'debt_name' is already in use.
            ImproperFunctionUse: Cannot add debt without setting plan duration first.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan to which you are trying to add a debt does not exist.")
        self.__plan_dict[plan_name].add_debt(debt_name)

    def delete_debt(self, plan_name, debt_name):
        """
        Removes a debt from a plan.

        Args:
            plan_name: Name of the plan.
            debt_name: Name of the debt to remove.

        Raises:
            NonexistentObject: It cannot delete a debt from a plan that does not exist.
            NonexistentObject: It cannot delete a debt which does not exist.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan from which you are trying to delete a debt does not exist.")
        self.__plan_dict[plan_name].delete_debt(debt_name)

    def set_debt_duration(self, plan_name, debt_name, start, end):
        """
        Sets the duration period for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            start: First month of debt (1-based index).
            end: Last month of debt (1-based index).

        Raises:
            NonexistentObject: It cannot edit a debt from a plan which does not exist.
            NonexistentObject: It cannot edit a debt which does not exist.
            InvalidValue: Start and end must be positive integers, with end greater than start.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan from which you are trying to edit does not exist.")
        if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
            raise NonexistentObject(f' there is no debt called "{debt_name}".')
        self.__plan_dict[plan_name].get_debt(debt_name).set_debt_duration(start, end)

    def set_debt_min_per_mth(self, plan_name, debt_name, minimum_per_month):
        """
        Sets the minimum monthly payment for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            minimum_per_month: Minimum payment per month.
        
        Raises:
            NonexistentObject: It cannot edit a debt from a plan which does not exist.
            NonexistentObject: It cannot edit a debt which does not exist.
            InvalidValue: Minimum per month must be a positive integer.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan from which you are trying to edit does not exist.")
        if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
            raise NonexistentObject(f' there is no debt called "{debt_name}".')
        self.__plan_dict[plan_name].get_debt(debt_name).set_debt_min_per_mth(minimum_per_month)

    def set_monthly_fee(self, plan_name, debt_name, monthly_fee):
        """
        Sets the monthly fee percentage for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            monthly_fee: Monthly fee percentage, between 0 and 100.
        
        Raises:
            NonexistentObject: It cannot edit a debt from a plan which does not exist.
            NonexistentObject: It cannot edit a debt which does not exist.
            InvalidValue: Monthly fee must be a positive percentage between 0 and 100.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan from which you are trying to edit does not exist.")
        if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
            raise NonexistentObject(f' there is no debt called "{debt_name}".')
        self.__plan_dict[plan_name].get_debt(debt_name).set_monthly_fee(monthly_fee)

    def set_delay_fee(self, plan_name, debt_name, delay_payment_fee):
        """
        Sets the delay payment fee for a debt.

        Args:
            plan_name: Name of the target plan.
            debt_name: Name of the debt.
            delay_payment_fee: Monthly fee percentage for late payments, between 0 and 100.
                
        Raises:
            NonexistentObject: It cannot edit a debt from a plan which does not exist.
            NonexistentObject: It cannot edit a debt which does not exist.
            InvalidValue: Delay fee must be a positive percentage between 0 and 100.
        """
        if not plan_name in self.__plan_dict.keys():
            raise NonexistentObject(" the plan from which you are trying to edit does not exist.")
        if not self.__plan_dict[plan_name].is_debt_in_the_plan(debt_name):
            raise NonexistentObject(f' there is no debt called "{debt_name}".')
        self.__plan_dict[plan_name].get_debt(debt_name).set_delay_fee(delay_payment_fee)

if __name__ == "__main__":

    pp = PrimoPobre()
    pp.create_plan("bad_timing")
    pp.add_debt("bad_timing", "credit_card")


