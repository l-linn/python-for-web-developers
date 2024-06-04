user_first_name = input('Enter your first name: ')
user_last_name = input('Enter your last name: ')
capitalised_user_first_name = user_first_name.capitalize()
capitalised_user_last_name = user_last_name.capitalize()

print('Hello, ' + capitalised_user_first_name + ' '+ capitalised_user_last_name)
print('Hello,',capitalised_user_first_name, capitalised_user_last_name)

# comma is a space
print(f'Hello, {capitalised_user_first_name} {capitalised_user_last_name}')
# string formatting: You use string formatting by including a set of opening and closing curly braces, {}, in the place where you want to add the value of a variable. To print a variable with a string in one line, you again include the character f in the same place – right before the quotation marks.
