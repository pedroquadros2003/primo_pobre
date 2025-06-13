class DebtStatsMaker:
    """
    Class that calculates statistics for debt data.
    """

    def __init__(self):
        pass

    def stats_debt(self, debt_data):
        """
        Calculate statistics for debt data
        Returns a dictionary with debt statistics

        Args:
            debt_data: List of Debt objects to analyze

        Returns:
            Dictionary containing:
            - total_debts: Number of debts
            - total_amount: Total amount to be paid across all debts
            - average_min_payment: Average minimum monthly payment
            - average_monthly_fee: Average monthly fee percentage
            - average_delay_fee: Average delay fee percentage
            - average_duration: Average debt duration in months
            - fully_specified_debts: Number of debts that are fully specified
            - debt_details: List of dictionaries with individual debt information
        """
        if not debt_data:
            return {
                'total_debts': 0,
                'total_amount': 0,
                'average_min_payment': 0,
                'average_monthly_fee': 0,
                'average_delay_fee': 0,
                'average_duration': 0,
                'fully_specified_debts': 0,
                'debt_details': []
            }

        total_amount = 0
        total_min_payment = 0
        total_monthly_fee = 0
        total_delay_fee = 0
        total_duration = 0
        fully_specified = 0
        debt_details = []

        for debt in debt_data:
            # Calculate total amount to pay
            total_amount += debt.get_total_to_pay()
            
            # Get minimum monthly payment
            min_payment = debt.get_min_per_mth()
            total_min_payment += min_payment
            
            # Get fees
            monthly_fee = debt.get_monthly_fee()
            delay_fee = debt.get_delay_fee()
            total_monthly_fee += monthly_fee
            total_delay_fee += delay_fee
            
            # Calculate duration
            duration = debt.get_debt_end() - debt.get_debt_start() + 1
            total_duration += duration
            
            # Check if debt is fully specified
            if debt.is_specified():
                fully_specified += 1
            
            # Add individual debt details
            debt_details.append({
                'name': debt.get_debt_name(),
                'total_to_pay': debt.get_total_to_pay(),
                'min_monthly_payment': min_payment,
                'monthly_fee': monthly_fee,
                'delay_fee': delay_fee,
                'duration': duration,
                'start_month': debt.get_debt_start(),
                'end_month': debt.get_debt_end(),
                'is_specified': debt.is_specified()
            })

        num_debts = len(debt_data)
        
        return {
            'total_debts': num_debts,
            'total_amount': total_amount,
            'average_min_payment': total_min_payment / num_debts,
            'average_monthly_fee': total_monthly_fee / num_debts,
            'average_delay_fee': total_delay_fee / num_debts,
            'average_duration': total_duration / num_debts,
            'fully_specified_debts': fully_specified,
            'debt_details': debt_details
        }
