from Plan import Plan
from Debt import Debt
from Exceptions_primo_pobre import *

class PlanSolver:
    """
    Solver class for financial plans. 
    Provides the interface for different implementations to solve debt payment plans.
    """

    def __init__(self):
        self.__implementation = 0

    def solve(self, plan):
        
        if not plan.get_is_duration_set():
            raise NotCompletelySpecified(" duration of the plan is not specified.")

        all_debts = plan.get_list_all_debts()

        for debt in all_debts:
            if not debt.is_specified():
                raise NotCompletelySpecified(" there are debt which were not completely specified.")
            if debt.get_debt_end() > plan.get_plan_duration():
                raise WronglySpecified(" there are debts which are due to months out of the plan duration.")
                        
        plan.set_solution_list(self.__implementation.solve(plan))




        