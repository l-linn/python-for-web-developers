months_named = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
months_numbered =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_dict = dict(zip (months_named, months_numbered))
months_named.clear()
months_numbered.clear()
print(months_dict)

months_extracted = list(months_dict.keys())
print(months_extracted)