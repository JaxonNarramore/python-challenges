print("Welcome to Jaxon bank.")

get_balance = input('Would you like to display your balance? (yes, no) ')

if get_balance in ('yes', 'no'):
    balance = int(4000)
    if get_balance == 'yes':
        print('Your current balance is', balance)
    elif get_balance == 'no':
        print('Okay broke boi')

todo = input('What would you like to do? (deposit, withdraw) ')

if todo in ('deposit', 'withdraw'):
    if todo == 'deposit':
        deposit = input('How much would you like to deposit? ')
        print(int(deposit) + int(balance))
    elif todo == 'withdraw':
        withdraw = input('How much would you like to withdraw? ')
        print(int(balance) - int(withdraw))
print("Have a nice day!")
