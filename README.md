# primo_pobre

PrimoPobre is a financial planning and debt management tool designed to help you organize your finances, track incomes and expenses, and strategize debt repayment. With PrimoPobre, you can create, manage, and analyze multiple financial plans to gain a clearer picture of your financial health.

---

## Authors

**COMP 27**

- Iago Jacob de Souza Ramos
- Marcelo Hippolyto de Sandes Peixoto
- Pedro Henrique Diogenes da Fonseca
- Pedro Ulisses de Lima Quadros
- Welberson Franklin Mello de Oliveira

Course: CSI-22 - Object-Oriented Programming  
Professor: Karla D. Fook  
Instituto Tecnológico de Aeronáutica

---

## Features

* **Create and Manage Plans**: Easily create new financial plans, copy existing ones, and delete plans you no longer need.
* **Detailed Plan Configuration**: Set the duration of your plans, define fixed monthly incomes and expenses, and add one-time incomes or expenses for specific months.
* **Comprehensive Debt Management**: Add multiple debts to each plan and specify their duration, minimum monthly payments, monthly fees, and delay payment fees.
* **Financial Problem Solver**: Utilize the built-in solver to analyze your financial plans, considering all incomes, expenses, and debts, to provide a structured solution.
* **Plan Persistence**: Save your financial plans to text files and load them back into the application for continued management.
* **Status Overview**: Get a complete overview of any plan, including its incomes, expenses, debts, and the calculated solution.
* **Statistical Analysis for Debts**: Utilize `DebtStatsMaker` to calculate and view detailed statistics about your debts, including total amounts, average payments, fees, and durations.

---

## How to Use

### Initialization

To start using PrimoPobre, you'll need to be in the project's main directory (primo_pobre/) and import the class.

* Navigate to the project directory:
  ```bash
  cd primo_pobre/
  ```
    
* Import the PrimoPobre class and create an instance:
    ```python
    from PrimoPobre import PrimoPobre    
    pp = PrimoPobre()
    ```

### Plan Management
 * Create a Plan:
    ```python
    pp.create_plan("MyFinancialPlan")
    ```

 * Copy a Plan:
    ```python
   pp.copy_plan("MyFinancialPlan", "RenamedPlan")
   ```

 * Delete a Plan:
    ```python
   pp.delete_plan("MyFinancialPlan")
   ```

 * List All Plans:
    ```python
   pp.list_plans()
   ```

 * Get Plan Status:
    ```python
   plan_info = pp.plan_status("MyFinancialPlan")
    print(plan_info) # This will print the detailed status of the plan
    ```

### Configuring a Plan
 * Set Plan Duration (in months):
    ```python
   pp.set_plan_duration("MyFinancialPlan", 12)
   ```

 * Set Monthly Incomes:
    ```python
   pp.set_monthly_incomes("MyFinancialPlan", 3000)
   ```

 * Set Monthly Expenses:
    ```python
   pp.set_monthly_expenses("MyFinancialPlan", 1500)
   ```

 * Add a Single Income:
    ```python
   pp.add_single_income("MyFinancialPlan", 500, 3) # Add 500 in month 3
   ```

 * Add a Single Expense:
    ```python
   pp.add_single_expense("MyFinancialPlan", 200, 6) # Add 200 in month 6
   ```

### Debt Management
 * Add a Debt:
    ```python
    pp.add_debt("MyFinancialPlan", "CreditCardDebt")
    ```

 * Delete a Debt:
    ```python
    pp.delete_debt("MyFinancialPlan", "CreditCardDebt")
    ```

 * Set Debt Duration (start and end month):
    ```python
    pp.set_debt_duration("MyFinancialPlan", "CreditCardDebt", 1, 6) # Debt from month 1 to 6
    ```

 * Set Minimum Monthly Payment for a Debt:
    ```python
    pp.set_debt_min_per_mth("MyFinancialPlan", "CreditCardDebt", 100)
    ```

 * Set Monthly Fee for a Debt (percentage):
    ```python
    pp.set_monthly_fee("MyFinancialPlan", "CreditCardDebt", 2.5) # 2.5% monthly fee
    ```

 * Set Delay Payment Fee for a Debt (percentage):
    ```python
    pp.set_delay_fee("MyFinancialPlan", "CreditCardDebt", 5.0) # 5.0% delay fee
    ```

### Solving and Saving
 * Solve a Plan:
    ```python
    pp.solve_plan("MyFinancialPlan")
    ```

   This will calculate the optimal way to pay off debts within the plan's constraints.

 * Save a Plan to a Text File:
    ```python
    pp.save_plan_txt("my_plan_backup", "MyFinancialPlan")
    ```

   This saves "MyFinancialPlan" to my_plan_backup.txt.

 * Load a Plan from a Text File:
    ```python
    pp.load_plan_txt("my_plan_backup.txt")
    ```
    
   This loads the plan saved in my_plan_backup.txt into PrimoPobre.
   
### Statistical Analysis for Debts
 * Get Debt Statistics:
```python
debt_stats = pp.get_debt_stats("MyFinancialPlan", "CreditCardDebt")
print(debt_stats) # This will print the detailed statistics of the debt
```

### Error Handling

  * NameError: When trying to create a plan with a name already in use, or a debt name that already exists within a plan.
  * NonexistentObject: When trying to interact with a plan or debt that doesn't exist.    
  * FileNotFoundError: When trying to load a plan from a file that doesn't exist.
  * ValueError: For invalid input values (e.g., non-positive amounts, incorrect percentages) or issues during file operations.
  * IndexError: When specifying a month outside the plan's defined duration.
  * ImproperFunctionUse: When attempting an action out of sequence (e.g., setting expenses before duration).
  * NotCompletelySpecified: When there is not sufficient information regarding the plan and its debts.
  * WronglySpecified: When there are debts due in months beyond the plan's duration.
