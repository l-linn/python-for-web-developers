user_input1 = int(input('Please enter the first number: '))
user_input2 = int(input('Please enter the seconde number: '))

user_input_operator = input ('Please choose your preffered operator between + and -: ')

if user_input_operator == '+':
  print(f'{user_input1} + {user_input2} = {user_input1 + user_input2}')
elif user_input_operator == '-':
  print(f'{user_input1} - {user_input2} = {user_input1 - user_input2}')
else:
  print('Sorry, unkown opperator!')