class Plan:
    """
    Represents a financial plan containing income, expenses, and debt information.
    The class maintains the state of a financial plan and provides methods to modify its parameters.
    Any modification to the plan's data will mark it as unsolved.
    """

    def __init__(self):
        """
        Initializes a new Plan instance with default values.
        """
        self.plan_name = ""
        self.monthly_expenses = 0
        self.monthly_incomes = 0
        self.plan_duration = 0
        self.single_income_list = []
        self.single_expense_list = []
        self.monthly_available_list = []
        self.debt_list = []
        self.solution_list = []
        self.is_solved = False

    def set_solution_list(self):
        """
        Calculates and sets the solution list for the plan based on current parameters.
        This method should mark the plan as solved upon successful completion.
        """
        pass

    def get_is_solved(self):
        """
        Returns the current solved status of the plan.

        Returns:
            bool: True if the plan has been solved, False otherwise.
        """
        pass

    def set_plan_duration(self, duration):
        """
        Sets the duration of the plan in months.
        Marks the plan as unsolved when called.

        Args:
            duration: Duration in months (positive integer)
        """
        pass

    def set_monthly_expenses(self, value):
        """
        Sets the amount for fixed monthly expenses.
        Marks the plan as unsolved when called.

        Args:
            value: Monthly expenses amount (non-negative float)
        """
        pass

    def set_monthly_incomes(self, value):
        """
        Sets the amount for fixed monthly incomes.
        Marks the plan as unsolved when called.

        Args:
            value: Monthly incomes amount (non-negative float)
        """
        pass

    def add_single_income(self, value, month):
        """
        Adds a one-time income entry for a specific month.
        Marks the plan as unsolved when called.

        Args:
            value: Income amount (non-negative float)
            month: Target month (1-based index, positive integer)
        """
        pass

    def add_single_expense(self, value, month):
        """
        Adds a one-time expense entry for a specific month.
        Marks the plan as unsolved when called.

        Args:
            value: Expense amount (non-negative float)
            month: Target month (1-based index, positive integer)
        """
        pass

    def add_debt(self, debt_name):
        """
        Adds a new debt to the plan.
        Marks the plan as unsolved when called.

        Args:
            debt_name: Identifier for the new debt
        """
        pass

    def delete_debt(self, debt_name):
        """
        Removes a debt from the plan.
        Marks the plan as unsolved when called.

        Args:
            debt_name: Identifier of the debt to remove
        """
        pass