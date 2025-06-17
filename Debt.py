from Exceptions_primo_pobre import *

class Debt:
    """
    Represents a debt instrument within a financial plan.
    Tracks all parameters of a debt including payment terms, fees, and duration.
    """

    def __init__(self, debt_name):

        self.__debt_name = debt_name 

        self.__debt_start = 0    ## first month in which the debt is going to be charged. At least 1

        self.__debt_end = 0      ## last month in which the debt is going to be charged. If greater than plan_duration, raises exception
                                 
        self.__min_per_mth = 0   ## minimum ammount to be payed per month

        self.__monthly_fee = 0   ## fees that are inherent to the debt, only to be considered in the case where it is != 0 (amortization)
                                 ## Its value lies between 0 and 100

        self.__delay_fee = 0     ## delay fee applied to delayed installments of a debt
                                 ## Its value lies between 0 and 100

        self.__total_to_pay = 0  ## minimum per month x (end - start + 1)

        self.__type = None


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
    
    def get_debt_start(self):
        return self.__debt_start
    
    def get_min_per_mth(self):
        return self.__min_per_mth
    
    def get_monthly_fee(self):
        return self.__monthly_fee
    
    def get_delay_fee(self):
        return self.__delay_fee
    
    def get_total_to_pay(self):
        return self.__total_to_pay
    
    def get_is_specified(self):
        return self.__is_specified

    def get_type(self):
        return self.__type
    
    def set_debt_duration(self, start, end):
        ## For the case where the end is greater than the duration of the plan, an exception will be raised
        ## inside the solve function, not here
       
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

        if self.__total_to_pay > 0 and self.__monthly_fee > 0:
            self.__type = (self.__delay_fee > 0) ? "complex" : "simple"
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
