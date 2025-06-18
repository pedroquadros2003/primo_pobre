from Plan import Plan
from Debt import Debt
from Exceptions_primo_pobre import *
from SolversImplementation.Implementation import *

class PlanSolver:
    """
    Solver class for financial plans. 
    Provides the interface for different implementations to solve debt payment plans.
    """

    def __init__(self):
        self.__implementation = Implementation_greedy_dc()

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

    def print_solution(self, plan):
        """
        Prints a detailed explanation of the plan's solution.
        
        Args:
            plan: The Plan object whose solution is to be printed.
        """
        solution_list = plan.get_solution_list()
        if not solution_list:
            print("\nNenhuma solução encontrada para o plano.")
            return

        print("\n=== SOLUÇÃO DO PLANO FINANCEIRO ===")
        print(f"Nome do Plano: {plan.get_name()}")
        print(f"Duração: {plan.get_plan_duration()} meses")
        print(f"Renda Mensal: R$ {plan.get_monthly_incomes():,.2f}")
        print(f"Despesas Mensais: R$ {plan.get_monthly_expenses():,.2f}")

        total_to_pay = 0;

        print("\n--- DETALHES DAS DÍVIDAS ---")
        for debt in plan.get_list_all_debts():
            print(f"\nDívida: {debt.get_debt_name()}")
            print(f"  Período: Mês {debt.get_debt_start()} até Mês {debt.get_debt_end()}")
            print(f"  Pagamento Mínimo Mensal: R$ {debt.get_min_per_mth():,.2f}")
            print(f"  Taxa Mensal: {debt.get_monthly_fee()}%")
            print(f"  Taxa de Atraso: {debt.get_delay_fee()}%")
            total_to_pay = total_to_pay + debt.get_total_to_pay()
            print(f"  Valor Total a Pagar: R$ {debt.get_total_to_pay():,.2f}")

        print("\n--- PLANO DE PAGAMENTO ---")
        
        # Dicionário para rastrear o total pago de cada dívida
        total_paid_per_debt = {debt.get_debt_name(): 0 for debt in plan.get_list_all_debts()}
        
        for month, payments in enumerate(solution_list, 1):
            print(f"\nMês {month}:")
            total_month = 0
            
            # Mostra o estado atual de cada dívida
            for debt in plan.get_list_all_debts():
                if debt.get_debt_start() <= month <= debt.get_debt_end():
                    # Calcula o valor total da dívida e juros acumulados
                    remaining_months = debt.get_debt_end() - month + 1
                    monthly_fee = debt.get_monthly_fee() / 100
                    total_debt = debt.get_min_per_mth() * remaining_months
                    accumulated_interest = total_debt * monthly_fee * remaining_months
                    
                    # Calcula o saldo devedor atual
                    total_with_interest = total_debt + accumulated_interest
                    remaining_balance = total_with_interest - total_paid_per_debt[debt.get_debt_name()]
                    
                    print(f"\n  Estado da dívida {debt.get_debt_name()}:")
                    print(f"    Valor total da dívida: R$ {total_debt:,.2f}")
                    print(f"    Juros acumulados: R$ {accumulated_interest:,.2f}")
                    print(f"    Total já pago: R$ {total_paid_per_debt[debt.get_debt_name()]:,.2f}")
                    print(f"    Saldo devedor atual: R$ {remaining_balance:,.2f}")
            
            # Mostra os pagamentos realizados e atualiza o total pago
            print("\n  Pagamentos realizados:")
            for debt_name, amount in payments.items():
                if amount > 0:
                    print(f"    {debt_name}: R$ {amount:,.2f}")
                    total_month += amount
                    total_paid_per_debt[debt_name] += amount
            
            print(f"\n  Total Pago no Mês: R$ {total_month:,.2f}")

        print("\n=== RESUMO FINAL ===")
        total_paid = sum(sum(month.values()) for month in solution_list)

        total_interest = total_paid - total_to_pay
        
        print(f"Valor Inicial Total das Dívidas: R$ {total_to_pay:,.2f}")
        print(f"Valor Total Pago: R$ {total_paid:,.2f}")
        print(f"Total de Juros Pagos: R$ {total_interest:,.2f}")
        print("=====================")




        
