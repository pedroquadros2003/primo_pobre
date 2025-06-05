class PlanStatsMaker:

    def __init__(self):
        pass

    def plan_status(self, plan):
        pass

    def stats_plan(self, plan_data):
        """
        Calculate statistics for plan data
        Returns a dictionary with plan statistics
        """
        stats = {
            'total_plans': len(plan_data),
            'active_plans': sum(1 for plan in plan_data if plan.get('status') == 'active'),
            'completed_plans': sum(1 for plan in plan_data if plan.get('status') == 'completed'),
            'total_investment': sum(plan.get('investment', 0) for plan in plan_data),
            'average_investment': sum(plan.get('investment', 0) for plan in plan_data) / len(plan_data) if plan_data else 0
        }
        return stats

    def stats_debt(self, debt_data):
        """
        Calculate statistics for debt data
        Returns a dictionary with debt statistics
        """
        stats = {
            'total_debt': sum(debt['amount'] for debt in debt_data),
            'number_of_debts': len(debt_data),
            'average_debt': sum(debt['amount'] for debt in debt_data) / len(debt_data) if debt_data else 0,
            'highest_debt': max((debt['amount'] for debt in debt_data), default=0),
            'lowest_debt': min((debt['amount'] for debt in debt_data), default=0)
        }
        return stats