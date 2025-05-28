class Debt:
    """
    Represents a debt instrument within a financial plan.
    Tracks all parameters of a debt including payment terms, fees, and duration.
    """

    def __init__(self, debt_name=""):

        self.debt_name = debt_name
        self.debt_start = 0
        self.debt_end = 0
        self.min_per_mth = 0
        self.monthly_fee = 0
        self.delay_fee = 0
        self.total_to_pay = 0
        self.is_specified = False  # Becomes True when all required parameters are set

    def set_debt_duration(self, start, end):
        
        pass

    def set_debt_value(self, value):
        
        pass

    def set_debt_min_per_mth(self, minimum_per_month):
        
        pass

    def set_monthly_fee(self, monthly_fee):
       
        pass

    def set_delay_fee(self, delay_payment_fee):
        
        pass

    def check_if_specified(self):
        """
        Verifies whether all required debt parameters have been set. While running, it updates the bool is_specified.

        Returns:
            bool: True if debt is fully specified, False otherwise

        """
        pass