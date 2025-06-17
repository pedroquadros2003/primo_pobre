import sys
from pathlib import Path

# Adiciona o diretório pai ao Python path
sys.path.append(str(Path(__file__).parent.parent))
from Plan import Plan

from abc import ABC, abstractmethod

class AbstractImplementation(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def solve(self, plan):
        ## the input is a plan, the output must be a solution_list,
        ## as in the example below
        month = 1
        debt_name = "banco"
        paid_amount = 130
        return None ## or return [ (debt_name, month, paid_ammount)]
                    ## this should be a list of tuples which correspond to the value 'paid_ammount' spent on 
                    ## paying off the debt 'debt_name' on the month 'month'
                    ## Return 'None' if there is no solution possible for the current plan
