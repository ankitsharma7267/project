
print('==========BALANCE ENQUIRY===========')

Menu = {
    1 : 'Check Balance',
    2 : 'Deposit',
    3 : 'Withdraw',
    4 : 'Exit'
}


amount = 10000
choice = int(input('Enter Your choice:'))

if choice == 1:
  print('Availabe Balance in your Account is :', amount)


elif choice == 2:
  deposit_amount = int(input('Enter the amount to deposit:'))
  amount += deposit_amount
  print('Deposit amount in your Account :', amount)
  

elif choice == 3:
  withdrawl_amount = int(input('Enter the amount you want to withdraw:'))

  if withdrawl_amount > amount:
    print('Insufficient Balance')

  else:
    amount -= withdrawl_amount
    print(f'The amount is withdraw from your account {withdrawl_amount} ')
    print('Your Available balance is:', amount)

elif choice == 4:
  print('Exit')


else:
  print('Invalid Choice')