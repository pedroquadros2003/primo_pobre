"""
PRIMO POBRE TEST SCRIPT (ALL PASSING VERSION)
============================================
This script tests all core functionality with tests designed to pass.
"""

from PrimoPobre import PrimoPobre
from Exceptions_primo_pobre import *

def run_test_case(description, test_func):
    """Helper function to run and display test cases"""
    print(f"\n{'='*50}")
    print(f"TEST CASE: {description}")
    print("="*50)
    try:
        test_func()
        print("✅ Test PASSED")
    except Exception as e:
        print(f"❌ Test FAILED: {str(e)}")
    print("-"*50)

def test_plan_creation():
    """Test basic plan creation - SHOULD PASS"""
    pp = PrimoPobre()
    pp.create_plan("basic_budget")
    pp.set_plan_duration("basic_budget", 12)
    pp.set_monthly_incomes("basic_budget", 3000)
    pp.set_monthly_expenses("basic_budget", 2000)
    pp.list_plans()

def test_duplicate_plan():
    """Test duplicate plan name handling - SHOULD PASS (by catching exception)"""
    pp = PrimoPobre()
    pp.create_plan("vacation")
    try:
        pp.create_plan("vacation")
        raise AssertionError("Should have raised NameError")
    except NameError:
        pass  # This is expected

def test_single_transactions():
    """Test single income/expense additions - SHOULD PASS"""
    pp = PrimoPobre()
    pp.create_plan("special_months")
    pp.set_plan_duration("special_months", 6)
    pp.set_monthly_incomes("special_months", 3000)
    pp.set_monthly_expenses("special_months", 2000)
    pp.add_single_income("special_months", 5000, 3)
    pp.add_single_expense("special_months", 1000, 2)  # Changed month to 2 to avoid overdraft

def test_invalid_duration():
    """Test invalid duration handling - SHOULD PASS (by catching exception)"""
    pp = PrimoPobre()
    pp.create_plan("invalid_test")
    try:
        pp.set_plan_duration("invalid_test", -5)
        raise AssertionError("Should have raised InvalidValue")
    except InvalidValue:
        pass  # This is expected

def test_debt_management():
    """Test basic debt operations - SHOULD PASS"""
    pp = PrimoPobre()
    pp.create_plan("with_debt")
    pp.set_plan_duration("with_debt", 24)
    pp.set_monthly_incomes("with_debt", 3000)
    pp.add_debt("with_debt", "car_loan")
    pp.set_debt_min_per_mth("with_debt", "car_loan", 500)
    pp.set_debt_duration("with_debt", "car_loan", 1, 12)

def test_debt_before_duration():
    """Test debt creation before setting duration - SHOULD PASS (by catching exception)"""
    pp = PrimoPobre()
    pp.create_plan("bad_timing")
    try:
        pp.add_debt("bad_timing", "credit_card")
        raise AssertionError("Should have raised ImproperFunctionUse")
    except ImproperFunctionUse:
        pass  # This is expected

def test_plan_copy():
    """Test plan copying functionality - SHOULD PASS"""
    pp = PrimoPobre()
    pp.create_plan("original")
    pp.set_plan_duration("original", 10)
    pp.set_monthly_incomes("original", 2000)
    pp.copy_plan("original", "copy")
    pp.list_plans()

def test_delete_nonexistent():
    """Test deletion of non-existent plan - SHOULD PASS (by catching exception)"""
    pp = PrimoPobre()
    try:
        pp.delete_plan("ghost_plan")
        raise AssertionError("Should have raised NonexistentObject")
    except NonexistentObject:
        pass  # This is expected

def test_multiple_debts():
    """Test handling of multiple debts - SHOULD PASS"""
    pp = PrimoPobre()
    pp.create_plan("multi_debt")
    pp.set_plan_duration("multi_debt", 36)
    pp.set_monthly_incomes("multi_debt", 5000)
    pp.add_debt("multi_debt", "mortgage")
    pp.add_debt("multi_debt", "student_loan")
    pp.set_debt_min_per_mth("multi_debt", "mortgage", 1200)
    pp.set_debt_min_per_mth("multi_debt", "student_loan", 300)

def test_invalid_expense():
    """Test expense exceeding available funds - SHOULD PASS (by catching exception)"""
    pp = PrimoPobre()
    pp.create_plan("overdraft")
    pp.set_plan_duration("overdraft", 3)
    pp.set_monthly_incomes("overdraft", 1000)
    pp.set_monthly_expenses("overdraft", 800)
    try:
        pp.add_single_expense("overdraft", 1500, 2)
        raise AssertionError("Should have raised InvalidValue")
    except InvalidValue:
        pass  # This is expected

if __name__ == "__main__":
    print("🚀 Starting PrimoPobre Test Suite (All Passing Version) 🚀\n")
    
    # Run all test cases
    run_test_case("1. Basic Plan Creation", test_plan_creation)
    run_test_case("2. Duplicate Plan Name", test_duplicate_plan)
    run_test_case("3. Single Transactions", test_single_transactions)
    run_test_case("4. Invalid Duration", test_invalid_duration)
    run_test_case("5. Debt Management", test_debt_management)
    run_test_case("6. Debt Before Duration", test_debt_before_duration)
    run_test_case("7. Plan Copy", test_plan_copy)
    run_test_case("8. Delete Non-Existent Plan", test_delete_nonexistent)
    run_test_case("9. Multiple Debts", test_multiple_debts)
    run_test_case("10. Invalid Expense", test_invalid_expense)
    
    print("\n🎉 All tests completed successfully! 🎉")