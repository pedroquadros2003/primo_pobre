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

    def create_plan(self, name):
        """
        Creates a new financial plan with the specified name.

        Args:
            name: Name of the plan to be created.

        Raises:
            NameError: This function cannot create a plan with a name already in use.
        """
        pass

    def copy_plan(self, source_name, target_name):
        """
        Copies an existing plan to a new one with other name.

        Args:
            source_name: Name of the original plan.
            target_name: Name of the new copy.

        Raises: 
            NameError: This function does not allow the copy to have the same name as the original.
        """
        pass

    def delete_plan(self, name):
        """
        Deletes an existing plan.

        Args:
            name: Name of the plan to be deleted.
        """
        pass

    def list_plans(self):
        """
        Lists all existing plans.

        Returns:
            List of all plan names.
        """
        pass

    def plan_status(self, name):
        """
        Returns the status of a specific plan.

        Args:
            name: Name of the plan to check.

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

    def solve_plan(self, name):
        """
        Solves a financial plan, considering all debts and available funds.

        Args:
            name: Name of the plan to solve.

        Note:
            If the plan was already solved with no changes, it does nothing.
            Checks debt validity before solving.
        """
        pass

    def set_plan_duration(self, plan, duration):
        """
        Sets the duration (in months) of a plan.

        Args:
            plan: Name of the plan.
            duration: Duration in months.
        """
        pass

    def set_monthly_expenses(self, plan, value):
        """
        Sets the fixed monthly expenses of a plan.

        Args:
            plan: Name of the plan.
            value: Monthly expenses value.
        """
        pass

    def set_monthly_incomes(self, plan, value):
        """
        Sets the fixed monthly incomes of a plan.

        Args:
            plan: Name of the plan.
            value: Monthly incomes value.
        """
        pass

    def add_single_income(self, plan, value, month):
        """
        Adds a one-time income to a specific month.

        Args:
            plan: Name of the plan.
            value: Income value.
            month: Target month (1-based index).
        """
        pass

    def add_single_expense(self, plan, value, month):
        """
        Adds a one-time expense to a specific month.

        Args:
            plan: Name of the plan.
            value: Expense value.
            month: Target month (1-based index).

        Raises:
            ValuError: This function cannot deduct more money than what is available to spend in the corresponding month.
        """
        pass

    def debt_status(self, debt_name, plan):
        """
        Presents the status of a debt.

        Args:
            debt_name: Name of the debt.
            plan: Name of the target plan.

        Returns:
            Total to pay, minimum per month, associatede fees and if it is completely specified.
        """

        pass
    
    def copy_debt(self, source_name, target_name):
        """
        Copies an existing debt to a new one with other name.

        Args:
            source_name: Name of the original plan.
            target_name: Name of the new copy.

        Note:
            If not specified, the target_name will be considered to be source_name+'_copy'.
        """
        pass

    def add_debt(self, debt_name, plan):
        """
        Adds a new debt to a plan.

        Args:
            debt_name: Name of the debt.
            plan: Name of the target plan.
        """
        pass

    def delete_debt(self, debt_name, plan):
        """
        Removes a debt from a plan.

        Args:
            debt_name: Name of the debt to remove.
            plan: Name of the plan.
        """
        pass

    def set_debt_duration(self, debt_name, start, end):
        """
        Sets the duration period for a debt.

        Args:
            debt_name: Name of the debt.
            start: First month of debt (1-based index).
            end: Last month of debt (1-based index).
        """
        pass


    def set_debt_min_per_mth(self, debt_name, minimum_per_month):
        """
        Sets the minimum monthly payment for a debt.

        Args:
            debt_name: Name of the debt.
            minimum_per_month: Minimum payment per month.
        """
        pass

    def set_monthly_fee(self, debt_name, monthly_fee):
        """
        Sets the monthly fee percentage for a debt.

        Args:
            debt_name: Name of the debt.
            monthly_fee: Monthly fee percentage, between 0 and .
        """
        pass

    def set_delay_fee(self, debt_name, delay_payment_fee):
        """
        Sets the delay payment fee for a debt.

        Args:
            debt_name: Name of the debt.
            delay_payment_fee: Monthly fee percentage for late payments, between 0 and 100.
        """
        pass




pp = PrimoPobre()