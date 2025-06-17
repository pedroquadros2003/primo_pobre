import sys
from pathlib import Path
from SolversImplementation.AbstractImplementation import AbstractImplementation
#this is supposed to be called fom parent directory

# Adiciona o diretório pai ao Python path
sys.path.append(str(Path(__file__).parent.parent))
from Plan import Plan

class Implementation(AbstractImplementation):

    def __init__(self):
        pass

    def solve(self, plan):
        ## the input is a plan, the output must be a solution_list,
        ## as in the example below
        monthly_available_list = plan.get_monthly_available_list()
        
        ret_list = [0]
        count = 1
        while count < plan.get_plan_duration():
            ret_list.append(("ababaca", count, monthly_available_list[count]))
            count = count + 1
        print("ecce planus:\n")
        print(ret_list);
        print(plan.get_debt_dict())
        return ret_list #None ## or return [ (debt_name, month, paid_ammount)]
                    ## this should be a list of tuples which correspond to the value 'paid_ammount' spent on 
                    ## paying off the debt 'debt_name' on the month 'month'
                    ## Return 'None' if there is no solution possible for the current plan
