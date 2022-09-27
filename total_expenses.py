import json

def total_expenses(monthly_expenses: dict) -> int:
    
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    
   
    x = list(monthly_expenses.values())
    return(sum(x)) 
f = open('data.json')
data = f.read()
data = json.loads(data) 
print(total_expenses(data))