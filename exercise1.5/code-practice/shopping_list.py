class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    shopping_list = []
    self.shopping_list = shopping_list
  
  def add_item(self, item):
    if item not in self.shopping_list:
      self.shopping_list.append(item)
      print('Item added successfully!')
      #or self.shopping_list = list(set(self.shopping_list.append(item)))?
    else:
      print('Item already in the list.')
    
    return self.shopping_list # do I need to return this?
  
  def remove_item(self, item):
    if item in self.shopping_list:
      self.shopping_list.remove(item)
      print('Item removed successfully!')
    else:
      print('Item not found')
  
  def view_list(self):
    print(self.list_name + ':')
    for item in self.shopping_list:
      print(f'- {item}')

  # add a new method that merges two shopping lists together
  def merge_lists(self, object):
    merged_lists_name = input('Create a name for the new list: ')

    #create an empty list for merged items
    merged_lists = ShoppingList(merged_lists_name)

    #copy the exsiting list into the empty list created above
    merged_lists.shopping_list = self.shopping_list.copy()

    for item in object.shopping_list:
      if item not in merged_lists.shopping_list:
        merged_lists.shopping_list.append(item)
    return merged_lists

#create objects using a pre defined class
pet_store_list = ShoppingList('Pet Store Shopping List')

pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

pet_store_list.remove_item('flea collars')

pet_store_list.add_item('frisbee')

pet_store_list.view_list()

grocery_store_list = ShoppingList('Grocery Store List')

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
  grocery_store_list.add_item(item)

# add a new method that merges two shopping lists together
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)
merged_list.view_list()
