from Exceptions_primo_pobre import *

class Debt:
    """
    Represents a debt instrument within a financial plan.
    Tracks all parameters of a debt including payment terms, fees, and duration.
    """

    def __init__(self, debt_name):

        self.__debt_name = debt_name
        self.__debt_start = 0
        self.__debt_end = 0
        self.__min_per_mth = 0
        self.__monthly_fee = 0
        self.__delay_fee = 0
        self.__total_to_pay = 0

    def copy(self, new_debt_name):
        
        aux = Debt(new_debt_name)
        
        aux.set_debt_duration(self.__debt_start, self.__debt_end)
        aux.set_debt_min_per_mth(self.__min_per_mth)
        aux.set_monthly_fee(self.__monthly_fee)
        aux.set_delay_fee(self.__delay_fee)

    def get_debt_name(self):
        return self.__debt_name
    
    def get_debt_end(self):
        return self.__debt_end

    def set_debt_duration(self, start, end):
        ## Wheter the end is greater than the duration of the plan or not, this exception will be raised
        ## inside the solve function
        
        if isinstance(start, int) and  isinstance(end, int) and start>=1 and end>=start:

            self.__debt_start = start
            self.__debt_end = end
            self.__total_to_pay = (end-start+1) * self.__min_per_mth

        else:
            raise InvalidValue(" start and end must positive integers, the latter greater than the former." )


    def set_debt_min_per_mth(self, minimum_per_month):
        
        if isinstance(minimum_per_month, int) and minimum_per_month > 0:

            self.__min_per_mth = minimum_per_month
            self.__total_to_pay = (self.__debt_end - self.__debt_start +1) * minimum_per_month

        else:
            raise InvalidValue(" minimum per month must be a positive integer.")

    def set_monthly_fee(self, monthly_fee):
       
        if isinstance(monthly_fee, float) and monthly_fee > 0 and monthly_fee<100:

            self.__monthly_fee = monthly_fee

        else:
            raise InvalidValue(" monthly fee must be a positive percentage between 0 and 100.")

    def set_delay_fee(self, delay_payment_fee):
        
        if isinstance(delay_payment_fee, float) and delay_payment_fee > 0 and delay_payment_fee<100:

            self.__delay_fee = delay_payment_fee

        else:
            raise InvalidValue(" delay fee must be a positive percentage between 0 and 100.")

    def is_specified(self):
        """
        Verifies whether all required debt parameters have been set. While running, it updates the bool is_specified.

        Returns:
            bool: True if debt is fully specified, False otherwise

        """

        if self.__total_to_pay > 0 and self.__monthly_fee>0:
            return True
        else:
            return False



if __name__ == "__main__":

    p = Debt("oss")

    p.set_debt_duration(14, 17)

    p.set_debt_min_per_mth(150)


    print(p.is_specified())

    p.set_monthly_fee(13.00)

    print(p.is_specified())