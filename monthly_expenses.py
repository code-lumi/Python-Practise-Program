monthly_expense = {"January": 2200, "February":2350, "March":2600, "April":2130, "May":2190}


print(len(monthly_expense))
'''
monthly_expense.update({"April": 2130 + 2005})
updated_april = monthly_expense
print(updated_april)

monthly_expense.update({"June": 1990})
updated_expenses = monthly_expense
print(updated_expenses)

for i in monthly_expense:
    if monthly_expense[i] == 2000:
        print(i) 
        '''

#total_expense_quater = monthly_expense["January"] + monthly_expense["February"] + monthly_expense["March"]
#print("Total expense in first quater was: ", total_expense_quater)

#extra_expenses_feburary = monthly_expense["February"] - monthly_expense["January"]
#print("The extra expense spent in febuary is: ", extra_expenses_feburary)