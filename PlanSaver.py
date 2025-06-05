
class PlanSaver:
    """
    Class that creates a .txt file from a plan
    """

    def __init__(self):
        pass

    def save_plan_txt(self, file_name, plan):
        """
        Saves a plan to a text file.

        Args:
            file_name: Name of the file to save to (without extension).
                      The file will be saved as file_name.txt.
            plan: The Plan object to save.

        Raises:
            ValueError: If the plan is invalid or if there's an error saving the file.
        """
        try:
            with open(f"{file_name}.txt", 'w') as file:
                # Write plan name
                file.write(f"{plan.get_name()}\n")
                
                # Write Plan section
                file.write("--Plan\n")
                file.write(f"duration: {plan.get_plan_duration()}\n")
                file.write(f"monthly_incomes: {plan.get_monthly_incomes()}\n")
                file.write(f"monthly_expenses: {plan.get_monthly_expenses()}\n")
                
                # Write single incomes
                for income in plan.get_single_income_list():
                    value, month = income
                    file.write(f"single_income: {value}, {month}\n")
                
                # Write single expenses
                for expense in plan.get_single_expense_list():
                    value, month = expense
                    file.write(f"single_expense: {value}, {month}\n")
                
                # Write Debts section
                file.write("--Debts\n")
                for debt_name, debt in plan.get_debt_dict().items():
                    file.write(f"debt: {debt_name}, {debt.get_debt_start()}, {debt.get_debt_end()}, "
                             f"{debt.get_min_per_mth()}, {debt.get_monthly_fee()}, {debt.get_delay_fee()}\n")
                
        except Exception as e:
            raise ValueError(f"Error saving plan: {str(e)}")