class PlanSolver:
    """
    Solver class for financial plans. 
    Provides the interface for different implementations to solve debt payment plans.
    """

    def solve(self, plan):

        pass

    def get_solution(self, plan):
        """
        Solves the plan and returns a detailed solution description.

        Args:
            plan: Instance of Plan to be solved

        Note:
            First calls solve() to calculate the solution, then formats the output
        """
        pass