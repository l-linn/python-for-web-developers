def guest_list(guest_name='unknown', age='unknown'): #Defining Functions with Default Arguments
  print('Guest Name: ' + guest_name)
  print('Age: ' + str(age))

guest_list('Craig', 46)
guest_list() #will return default arguments
#Guest Name: unknown
#Age: unknown

user_destination = input('Where do you want to go?\n') #start a new line using \n
if user_destination == 'New York' or user_destination == 'London' or user_destination == 'Tokyo':
  print('Enjoy your stay in ' + user_destination + '!')
else: 
  print('Oops, that destination is not currently available.')
