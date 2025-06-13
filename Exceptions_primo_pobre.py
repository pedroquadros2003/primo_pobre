"""
Custom exceptions for the Primo Pobre project.
These exceptions are used to handle specific error cases in the financial planning system.
"""

class ImproperInput(Exception):
    pass

class ImproperFunctionUse(Exception):
    """
    Raised when a function is called in an incorrect order or context.
    
    This exception is used when:
    - Trying to set monthly incomes/expenses before setting plan duration
    - Trying to add single incomes/expenses before setting plan duration
    - Trying to add debts before setting plan duration
    - Trying to redefine plan duration after it's already set
    """
    pass

class InvalidValue(Exception):
    """
    Raised when a value is invalid for a specific parameter.
    
    This exception is used when:
    - Duration is not a positive integer
    - Monthly incomes/expenses are not positive integers
    - Monthly expenses exceed monthly incomes
    - Single income/expense values are not positive integers
    - Debt parameters (min_per_month, monthly_fee, delay_fee) are invalid
    - Debt duration (start/end) is invalid
    """
    pass

class InvalidName(Exception):
    pass

class NonexistentObject(Exception):
    """
    Raised when trying to access or modify an object that doesn't exist.
    
    This exception is used when:
    - Trying to access a plan that doesn't exist
    - Trying to access a debt that doesn't exist in a plan
    - Trying to delete a non-existent plan or debt
    """
    pass

class NotCompletelySpecified(Exception):
    """
    Raised when a plan or debt is not fully specified.
    
    This exception is used when:
    - Plan duration is not set
    - Debt parameters are not all set (duration, min_per_month, fees)
    - Required plan parameters are missing
    """
    pass

class WronglySpecified(Exception):
    """
    Raised when a plan or debt is specified incorrectly.
    
    This exception is used when:
    - Debt duration extends beyond plan duration
    - Monthly expenses exceed monthly incomes
    - Single expenses exceed available funds
    - Invalid combinations of parameters
    """
    pass

class FileOperationError(Exception):
    """
    Raised when there are issues with file operations.
    
    This exception is used when:
    - File not found during loading
    - Invalid file format
    - Permission issues
    - I/O errors
    """
    pass

class DuplicateNameError(Exception):
    """
    Raised when trying to create an object with a name that already exists.
    
    This exception is used when:
    - Creating a plan with an existing name
    - Adding a debt with a name already in use
    - Loading a plan with a name that already exists
    """
    pass

class InsufficientFundsError(Exception):
    """
    Raised when there are not enough funds for an operation.
    
    This exception is used when:
    - Adding an expense that exceeds available funds
    - Setting monthly expenses higher than monthly incomes
    - Debt payments exceed available funds
    """
    pass

class InvalidDateError(Exception):
    """
    Raised when date-related parameters are invalid.
    
    This exception is used when:
    - Month index is out of plan duration
    - Debt start/end months are invalid
    - Invalid date ranges
    """
    pass