from Plan import Plan


class PlanLoader:
    """
    Class that creates a plan from .txt file
    """

    def __init__(self):
        pass

    def load_plan_txt(self, file_name):
        """
        Loads a plan from a text file.

        Args:
            file_name: Name of the file to load (without extension).
                      The file should be named file_name.txt.

        Returns:
            A Plan object with the loaded data.

        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            ValueError: If the file format is invalid.
        """
        try:
            with open(f"{file_name}.txt", 'r') as file:
                lines = file.readlines()
                
                # First line should be the plan name
                plan_name = lines[0].strip()
                plan = Plan(plan_name)
                
                # Parse the rest of the file
                current_section = None
                for line in lines[1:]:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue
                        
                    if line.startswith('--'):  # Section header
                        current_section = line[2:].strip()
                        continue
                        
                    if current_section == 'Plan':
                        # Parse plan parameters
                        if line.startswith('duration:'):
                            duration = int(line.split(':')[1].strip())
                            plan.set_plan_duration(duration)
                        elif line.startswith('monthly_incomes:'):
                            incomes = int(line.split(':')[1].strip())
                            plan.set_monthly_incomes(incomes)
                        elif line.startswith('monthly_expenses:'):
                            expenses = int(line.split(':')[1].strip())
                            plan.set_monthly_expenses(expenses)
                        elif line.startswith('single_income:'):
                            # Format: single_income: value, month
                            parts = line.split(':')[1].strip().split(',')
                            value = int(parts[0].strip())
                            month = int(parts[1].strip())
                            plan.add_single_income(value, month)
                        elif line.startswith('single_expense:'):
                            # Format: single_expense: value, month
                            parts = line.split(':')[1].strip().split(',')
                            value = int(parts[0].strip())
                            month = int(parts[1].strip())
                            plan.add_single_expense(value, month)
                            
                    elif current_section == 'Debts':
                        # Parse debt information
                        if line.startswith('debt:'):
                            # Format: debt: name, start_month, end_month, min_per_month, monthly_fee, delay_fee
                            parts = line.split(':')[1].strip().split(',')
                            debt_name = parts[0].strip()
                            start_month = int(parts[1].strip())
                            end_month = int(parts[2].strip())
                            min_per_month = int(parts[3].strip())
                            monthly_fee = int(parts[4].strip())
                            delay_fee = int(parts[5].strip())
                            
                            plan.add_debt(debt_name)
                            debt = plan.get_debt(debt_name)
                            debt.set_debt_duration(start_month, end_month)
                            debt.set_debt_min_per_mth(min_per_month)
                            debt.set_monthly_fee(monthly_fee)
                            debt.set_delay_fee(delay_fee)
                
                return plan
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Plan file {file_name}.txt not found")
        except Exception as e:
            raise ValueError(f"Error loading plan: {str(e)}")