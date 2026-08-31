
print('==============EXPENSE TRACKER==============')


Expense = [
    ['Food' , 150],
    ['Travel' , 50],
    ['College' , 100],
    ['Food' , 200]
]


choice = input('Enter the choice of your Expense:')
total_expense = 0


if choice == 'Food':
  total_expense = Expense[0][1] + Expense[3][1]
  print('Expenses of Food is:', total_expense)


elif choice == 'Travel':
  total_expense = Expense[1][1]
  print('Expense over Traveling is:', total_expense)


elif choice == 'College':
  total_expense = Expense[2][1]
  print('Expense over college is:', total_expense)


else:
  print('Invalid Input')