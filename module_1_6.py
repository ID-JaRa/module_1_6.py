my_dict = {'Misha': 2_03_1988, 'Masha': 7_12_1999,
           'Vika': 6_04_2001, 'Anna': 2_05_1997}
print(my_dict)
print(my_dict.get ('Anna'))
print(my_dict.get('Kira'))
my_dict.update({'Bella': 7_07_2022, 'Dasha': 15_11_2020})
print(my_dict)
sister = my_dict.pop('Vika')
print(sister)
print(my_dict)


my_set = {1, 2, 2, 9, 5, 9, 'ID', False, 'ID', 2, 2}
print(my_set)
my_set.add(4)
my_set.add(7)
my_set.remove(2)
print(my_set)