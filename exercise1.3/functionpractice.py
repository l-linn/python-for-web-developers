def guest_list(guest_name='unknown', age='unknown'): #Defining Functions with Default Arguments
  print('Guest Name: ' + guest_name)
  print('Age: ' + str(age))

guest_list('Craig', 46)
guest_list() #will return default arguments
#Guest Name: unknown
#Age: unknown