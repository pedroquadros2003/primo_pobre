class PlanStatsMaker:

    def __init__(self):
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